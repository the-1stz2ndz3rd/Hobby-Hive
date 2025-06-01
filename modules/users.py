# modules/users.py
from utils.data_storage import load_json

USERS_FILE = "data/users_data.json"

def get_all_users():
    return load_json(USERS_FILE)

def user_exists(username):
    users = load_json(USERS_FILE)
    return username in users
