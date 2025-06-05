import json
import os
from chama.data_handler import load_data, save_data

CHAMA_FILE = 'chama_data.json'

def load_chamas():
    if not os.path.exists(CHAMA_FILE):
        return {}
    return load_data(CHAMA_FILE)

def save_chamas(data):
    save_data(CHAMA_FILE, data)

def load_chamas_for_user(email):
    data = load_chamas()
    return data.get(email, [])

def create_chama_for_user(email, chama_name):
    data = load_chamas()
    user_chamas = data.get(email, [])
    new_chama = {
        "id": len(user_chamas) + 1,
        "name": chama_name,
        "members": [],
        "transactions": []
    }
    user_chamas.append(new_chama)
    data[email] = user_chamas
    save_chamas(data)
