from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from utils.models import Admin, Base  # adjust this import based on your project structure
from utils.db import SessionLocal
from argon2 import PasswordHasher
import os




def create_admin(username, email, password):
    # Create a new session
    db = SessionLocal()
    try:
        # Check if the admin already exists
        existing_admin = db.query(Admin).filter(Admin.username == username).first()
        if existing_admin:
            print(f"Admin with username '{username}' already exists.")
            return

        # Create a new admin instance
        new_admin = Admin(username=username, email=email)
        new_admin.set_password(password)  # Hash the password

        # Add and commit the new admin to the database
        db.add(new_admin)
        db.commit()
        print(f"Admin '{username}' created successfully.")
    except Exception as e:
        db.rollback()  # Rollback in case of error
        print(f"Error creating admin: {e}")
    finally:
        db.close()  # Close the session
if __name__ == "__main__":
    # Replace with your desired admin credentials
    create_admin(username="priyanshu", email="priyanshu1@gmail.com", password="Priyanshu123")
