from flask import Blueprint, request, jsonify, make_response
from utils.db import SessionLocal
from utils.models import Admin
from utils.jwt import generate_token
from sqlalchemy.orm import Session
import re

auth_blueprint = Blueprint('auth', __name__)

def is_valid_email(email: str) -> bool:
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

@auth_blueprint.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400

    data = request.get_json()

    email = data.get("email", "").strip()
    password = data.get("password", "")

    # === Basic validation ===
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    db: Session = SessionLocal()
    try:
        admin = db.query(Admin).filter(Admin.email == email).first()

        if not admin or not admin.check_password(password):
            # Optional: log failed attempt
            return jsonify({"error": "Invalid email or password"}), 401

        token = generate_token(admin.id)

        response = make_response(jsonify({
            "message": "Login successful",
            "admin" : admin.as_dict(),  # Assuming Admin model has a to_dict() method
            
        }), 200)
        response.set_cookie(
            "auth_token",
            token,
            httponly=True,
            secure=False,  
            samesite='Lax', 
            max_age=86400,  
            path='/'  
        )
        print(response)
        return response

    except Exception as e:
        print(f"Error during login: {str(e)}")
        return jsonify({"error": f"Internal server error"}), 500

    finally:
        db.close()

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({"message": "Logged out successfully"}))
    response.set_cookie(
        "auth_token",
        "",
        max_age=0,
        httponly=True,
        samesite='Lax',
        path='/'
    )
    return response
