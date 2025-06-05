import json
import os

DATA_FILE = "chama_data.json"

def save_data(data, filename=DATA_FILE):
    """
    Save data list to JSON file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filename=DATA_FILE):
    """
    Load and return data list from JSON file.
    """
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
    return []


