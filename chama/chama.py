import json
import os

DATA_FILE = "chama_data.json"

# Ensure the file exists
def init_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)

# Load chama data
def load_data():
    init_data_file()
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save chama data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Load all chamas for a user
def load_chamas_for_user(email):
    data = load_data()
    return data.get(email, {}).get("chamas", [])

# Create a new chama for a user
def create_chama_for_user(email, chama_name):
    data = load_data()
    if email not in data:
        data[email] = {"chamas": []}
    data[email]["chamas"].append({
        "name": chama_name,
        "members": [],
        "transactions": []
    })
    save_data(data)
