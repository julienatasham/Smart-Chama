import json
import os

def save_data(data, filename="chama_data.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filename="chama_data.json"):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
    return []

