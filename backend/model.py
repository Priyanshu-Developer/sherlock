from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Wafunnel(Base):
    __tablename__ = "Wafunnel"
    __table_args__ = {"schema": "Sherlocksauto"}  # Set schema

    number = Column(String(255), primary_key=True)  # Assuming this is unique
    stage = Column(Integer)
    date = Column(Date)
