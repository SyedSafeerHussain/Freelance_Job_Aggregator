import schedule
import os
import logging
import time
import subprocess

# Setup logging for scheduler

LOG_DIR="logs"
os.makedirs(LOG_DIR,exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR,"scheduler.log"),
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
def job():
    logging.info("🟢 Starting main.py run...")
    try:
        subprocess.run(["python","main.py"],check=True)
        logging.info("✅ main.py finished successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to run main.py: {str(e)}")
    
schedule.every(10).minutes.do(job)

logging.info("🚀 Scheduler started. Waiting for next run...")
