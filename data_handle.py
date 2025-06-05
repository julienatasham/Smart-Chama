import json
import os

def save_data(data, filename="chama_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename="chama_data.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []  # If file doesn’t exist, return an empty list
