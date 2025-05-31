# modules/user_auth.py
from utils.validation import is_valid_signup, is_valid_login
from utils.data_storage import load_json, save_json

USERS_FILE = "data/users_data.json"

def signup(user_data):
    """
    user_data is dict with keys:
    name, student_id, username, password, bio, hobbies (list)
    """
    users = load_json(USERS_FILE)

    if user_data["username"] in users:
        return False, "Username already exists."

    valid, msg = is_valid_signup(user_data)
    if not valid:
        return False, msg

    users[user_data["username"]] = user_data
    save_json(USERS_FILE, users)
    return True, "Account created successfully."

def login(username, password):
    users = load_json(USERS_FILE)

    valid, msg = is_valid_login(username, password)
    if not valid:
        return False, msg

    if username not in users or users[username]["password"] != password:
        return False, "Invalid username or password."

    return True, "Login successful."
