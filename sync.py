import json
from dsn_connector import fetch_data
from api_client import push_data
from utils import log, setup_logging
from concurrent.futures import ThreadPoolExecutor, as_completed

def sync_single_source(source):
    """Sync a single source"""
    try:
        log(f"🔗 Syncing {source['name']} ...")
        data = fetch_data(source)
        
        if data:
            push_data(source, data)
            return True
        else:
            log(f"⚠️ No data for {source['name']}")
            return False
    except Exception as e:
        log(f"🔥 Error syncing {source['name']}: {e}")
        return False

def run_sync():
    setup_logging()
    log("🚀 Starting Fast Sync Process")

    try:
        with open("config.json") as f:
            config = json.load(f)
    except Exception as e:
        log(f"❌ Error loading config.json: {e}")
        return

    sources = config.get("sources", [])
    
    # Sync sources in parallel (2 at a time)
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(sync_single_source, source) for source in sources]
        
        successful = 0
        for future in as_completed(futures):
            if future.result():
                successful += 1
    
    log(f"✅ Sync completed: {successful}/{len(sources)} sources successful")

if __name__ == "__main__":
    run_sync()