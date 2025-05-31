# modules/search.py
from utils.data_storage import load_json

USERS_FILE = "data/users_data.json"
GROUPS_FILE = "data/group_data.json"

def search_users_by_name(query):
    users = load_json(USERS_FILE)
    return {u: data for u, data in users.items() if query.lower() in u.lower()}

def search_groups_by_name(query):
    groups = load_json(GROUPS_FILE)
    return {g: details for g, details in groups.items() if query.lower() in g.lower()}

def search_users_by_hobby(hobby):
    users = load_json(USERS_FILE)
    hobby_lower = hobby.lower()
    return {
        u: data for u, data in users.items()
        if any(h.lower() == hobby_lower for h in data.get("hobbies", []))
    }
