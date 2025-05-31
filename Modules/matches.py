# modules/matches.py
from utils.data_storage import load_json

USERS_FILE = "data/users_data.json"

def find_matches(username):
    users = load_json(USERS_FILE)
    if username not in users:
        return []

    user_hobbies = set(h.lower() for h in users[username].get("hobbies", []))
    matches = []

    for other_user, data in users.items():
        if other_user == username:
            continue
        other_hobbies = set(h.lower() for h in data.get("hobbies", []))
        common = user_hobbies.intersection(other_hobbies)
        if len(common) >= 2:
            matches.append({"username": other_user, "common_hobbies": list(common)})

    return matches
