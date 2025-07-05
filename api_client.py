import requests
import time
from utils import log
from concurrent.futures import ThreadPoolExecutor, as_completed

# Use a persistent session for faster requests
session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})

def push_chunk(args):
    """Push a single chunk - for threading"""
    chunk, url, chunk_id, source_name = args
    try:
        response = session.post(url, json=chunk, timeout=60)
        if response.status_code in [200, 201]:
            log(f"✅ {source_name} - Chunk {chunk_id} pushed ({len(chunk)} records)")
            return True
        else:
            log(f"❌ {source_name} - Chunk {chunk_id} failed - {response.status_code}")
            return False
    except Exception as e:
        log(f"❌ {source_name} - Chunk {chunk_id} error: {e}")
        return False

def push_data(source, data, chunk_size=1000, max_workers=3):  # Increased chunk size
    log(f"📤 Pushing data to {source['name']} API...")
    
    if not data:
        return
    
    total_records = len(data)
    start_time = time.time()
    
    # Create chunks
    chunks = []
    for i in range(0, total_records, chunk_size):
        chunk = data[i:i + chunk_size]
        chunks.append((chunk, source['api_url'], i // chunk_size + 1, source['name']))
    
    # Push chunks in parallel
    successful = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(push_chunk, chunk_args) for chunk_args in chunks]
        
        for future in as_completed(futures):
            if future.result():
                successful += 1
    
    total_elapsed = round(time.time() - start_time, 2)
    log(f"✅ {source['name']}: {successful}/{len(chunks)} chunks pushed in {total_elapsed}s")