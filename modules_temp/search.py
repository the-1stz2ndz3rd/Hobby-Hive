# modules/search.py

from utils.data_storage import load_json

USERS_FILE = "data/users_data.json"
GROUPS_FILE = "data/group_data.json"

def search_users_by_name(query: str) -> dict:
    """
    Search users whose usernames contain the query string (case-insensitive).
    """
    users = load_json(USERS_FILE)
    if not isinstance(users, dict):
        return {}
    query_lower = query.lower()
    return {u: data for u, data in users.items() if query_lower in u.lower()}

def search_groups_by_name(query: str) -> dict:
    """
    Search groups whose names contain the query string (case-insensitive).
    """
    groups = load_json(GROUPS_FILE)
    if not isinstance(groups, dict):
        return {}
    query_lower = query.lower()
    return {g: details for g, details in groups.items() if query_lower in g.lower()}

def search_users_by_hobby(hobby: str) -> dict:
    """
    Search users who have the given hobby (case-insensitive exact match).
    """
    users = load_json(USERS_FILE)
    if not isinstance(users, dict):
        return {}
    hobby_lower = hobby.lower()
    return {
        u: data for u, data in users.items()
        if any(h.lower() == hobby_lower for h in data.get("hobbies", []))
    }
