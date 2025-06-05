import json
import os
import bcrypt

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register_user(email: str, password: str) -> bool:
    users = load_users()
    if email in users:
        return False  # User already exists
    users[email] = hash_password(password)
    save_users(users)
    return True

def login_user(email: str, password: str) -> bool:
    users = load_users()
    if email not in users:
        return False
    hashed = users[email]
    return check_password(password, hashed)
