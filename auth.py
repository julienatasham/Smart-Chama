import json
import os
import bcrypt

# File to store user credentials
USERS_FILE = 'users.json'

# Load all users from the file
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

# Save all users to the file
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Hash a plain-text password (used during registration)
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

# Check if plain-text password matches hashed one (used during login)
def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Register a new user (returns True if successful, False if email already exists)
def register_user(email: str, password: str) -> bool:
    users = load_users()
    if email in users:
        return False  # Email already registered
    users[email] = hash_password(password)
    save_users(users)
    return True

# Log in a user (returns True if email exists and password is correct)
def login_user(email: str, password: str) -> bool:
    users = load_users()
    if email not in users:
        return False
    hashed = users[email]
    return check_password(password, hashed)
