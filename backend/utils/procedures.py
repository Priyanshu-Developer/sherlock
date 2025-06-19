from .db import SessionLocal
from sqlalchemy import text

def assignment_procedure():
    db = SessionLocal()
    try:
        result = db.execute(text("EXEC sp_assign_wafunnel_to_agents"))
        return result.fetchall()
    finally:
        db.close()
