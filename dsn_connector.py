import pyodbc
import time
from utils import log
from table_mapping import TABLE_MAPPING
from decimal import Decimal

def safe_convert(value):
    if isinstance(value, Decimal):
        return float(value)
    return value

def connect_with_retry(dsn, retries=3, delay=5):
    for attempt in range(retries):
        try:
            log(f"🔌 Attempting connection to DSN '{dsn}' (try {attempt + 1})...")
            conn = pyodbc.connect(
                f"DSN={dsn};ConnectionTimeout=30",  # Increased timeout
                autocommit=True
            )
            log(f"✅ Connected to DSN '{dsn}' successfully.")
            return conn
        except pyodbc.Error as e:
            log(f"⚠️ Connection attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                log(f"⏳ Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise

def fetch_data(source, batch_size=2000):  # Increased batch size
    try:
        source_config = TABLE_MAPPING.get(source['name'])
        if not source_config:
            log(f"❌ No table mapping found for {source['name']}")
            return None

        conn = connect_with_retry(source['dsn'], retries=3, delay=5)
        cursor = conn.cursor()

        table = source_config['table']
        columns = source_config.get('columns', '*')
        condition = source_config.get('condition')

        query = f"SELECT {columns} FROM {table}"
        if condition:
            query += f" WHERE {condition}"

        log(f"🔍 Running Query on {source['name']}: {query}")
        cursor.execute(query)

        column_names = [column[0] for column in cursor.description]
        data = []

        # Fetch all at once if small dataset, otherwise batch
        try:
            # Try to fetch all first (faster for small datasets)
            all_rows = cursor.fetchall()
            for row in all_rows:
                record = {col: safe_convert(val) for col, val in zip(column_names, row)}
                data.append(record)
            log(f"✅ Fetched {len(data)} rows from {source['name']} at once")
        except:
            # Fallback to batch processing
            batch_num = 1
            while True:
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                for row in rows:
                    record = {col: safe_convert(val) for col, val in zip(column_names, row)}
                    data.append(record)
                log(f"📦 Batch {batch_num} fetched with {len(rows)} records.")
                batch_num += 1

        conn.close()
        return data

    except Exception as e:
        log(f"❌ Error fetching data from {source['name']}: {e}")
        return None
