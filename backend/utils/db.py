# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import URL
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
import os

load_dotenv()

Base = declarative_base()

# Create connection URL
__DATABASE_URL = URL.create(
    drivername="mssql+pymssql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_SERVER"),
    port=os.getenv("DB_PORT", 1433),
    database=os.getenv("DB_NAME"),
  
)

# Create a persistent engine
engine = create_engine(__DATABASE_URL, echo=False, pool_pre_ping=True)

# Create a factory for sessions
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
