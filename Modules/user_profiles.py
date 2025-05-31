# modules/user_profiles.py
from utils.data_storage import load_json, save_json

USERS_FILE = "data/users_data.json"

def get_user_profile(username):
    users = load_json(USERS_FILE)
    return users.get(username)

def update_user_profile(username, updates):
    """
    updates: dict with keys like 'bio', 'hobbies' (list), etc.
    """
    users = load_json(USERS_FILE)
    if username not in users:
        return False, "User not found."

    user = users[username]
    for key, value in updates.items():
        if key in user:
            user[key] = value

    users[username] = user
    save_json(USERS_FILE, users)
    return True, "Profile updated successfully."
