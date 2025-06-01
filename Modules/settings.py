# modules/settings.py
from utils.data_storage import load_json, save_json

USERS_FILE = "data/users_data.json"

def get_user_settings(username):
    users = load_json(USERS_FILE)
    user = users.get(username, {})
    settings = user.get("settings", {"dark_mode": False})
    return settings

def toggle_dark_mode(username):
    users = load_json(USERS_FILE)
    user = users.get(username)
    if not user:
        return False  # User not found

    settings = user.get("settings", {"dark_mode": False})
    settings["dark_mode"] = not settings.get("dark_mode", False)
    user["settings"] = settings
    users[username] = user
    save_json(USERS_FILE, users)
    return settings["dark_mode"]
