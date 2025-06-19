# models.py
from sqlalchemy import Column, Integer, String, DateTime
from .db import Base
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import datetime

class WAFunnel(Base):
    __tablename__ = 'Wafunnel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(20), nullable=False)
    stage = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<WAFunnel(id={self.id}, number={self.number}, stage={self.stage})>"

    def as_dict(self):
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        # Accept both datetime.datetime and datetime.date
        if isinstance(result.get("date"), (datetime.datetime, datetime.date)):
            result["date"] = result["date"].strftime("%d %B %Y")

        return result



ph = PasswordHasher()

class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)  # Stores Argon2 hash
    email = Column(String(100), nullable=False, unique=True)

    def set_password(self, plain_password: str):
        self.password = ph.hash(plain_password)

    def check_password(self, plain_password: str) -> bool:
        try:
            return ph.verify(self.password, plain_password)
        except VerifyMismatchError:
            return False

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

class AgentWAFunnelAssignment(Base):
    __tablename__ = 'agent_wafunnel_assignment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent = Column(String(100), nullable=False)
    Number = Column(String(20), nullable=False)  # Will alias this as phoneNo when returning

    def as_dict(self):
        return {
            "id": self.id,
            "agent": self.agent,
            "phoneNo": self.Number  # aliasing 'Number' as 'phoneNo'
        }
