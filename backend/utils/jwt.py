from functools import wraps
import jwt
import datetime
from dotenv import load_dotenv
import os 
from flask import request, jsonify,g
from functools import wraps

load_dotenv()

def generate_token(admin_id: int, expires_in: int = 3600):
        
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is not set in the environment variables.")
    if admin_id is None:
        raise ValueError("admin_id must be provided to generate a token.")
    payload = {
        "admin_id": admin_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str):

    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is not set in the environment variables.")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["admin_id"]
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token



def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 🍪 Get token from the cookie
        token = request.cookies.get("auth_token")

        if not token:
            return jsonify({"error": "Missing authentication token"}), 401

        admin_id = decode_token(token)

        if not admin_id:
            return jsonify({"error": "Invalid or expired token"}), 401

        g.admin_id = admin_id  # 🧠 Store admin_id for use in routes
        return f(*args, **kwargs)

    return decorated_function