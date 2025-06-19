from apscheduler.schedulers.background import BackgroundScheduler
from .db import engine
from sqlalchemy import text
from datetime import datetime

def run_stored_procedure() -> bool:
    """Executes the stored procedure to assign leads to agents.
    Returns True if successful, False otherwise.
    """
    print(f"[{datetime.now()}] Starting stored procedure execution...")
    try:
        print(f"[{datetime.now()}] Running stored procedure...")
        with engine.connect() as conn:
            conn.execute(text("EXEC sp_assign_wafunnel_to_agents"))
            print("✅ Stored procedure executed successfully.")
            return True
    except Exception as e:
        print("❌ Failed to execute stored procedure:", e)
        return False

def schedule_daily_task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=run_stored_procedure,
        trigger='cron',
        hour=20,
        minute=40,
        id='daily_wafunnel_assignment'
    )
    scheduler.start()
    print("🕒 Scheduler started. Procedure will run every day at 8:40 PM.")
