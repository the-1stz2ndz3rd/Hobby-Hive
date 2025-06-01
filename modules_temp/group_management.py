# modules/group_management.py
from utils.data_storage import load_json, save_json

GROUPS_FILE = "data/group_data.json"

def get_all_groups():
    return load_json(GROUPS_FILE)

def get_group_by_name(group_name):
    groups = load_json(GROUPS_FILE)
    return groups.get(group_name)

def create_group(group_name, details):
    groups = load_json(GROUPS_FILE)
    if group_name in groups:
        return False, "Group already exists."
    groups[group_name] = details
    save_json(GROUPS_FILE, groups)
    return True, "Group created."

def update_group(group_name, updates):
    groups = load_json(GROUPS_FILE)
    if group_name not in groups:
        return False, "Group not found."

    group = groups[group_name]
    for key, value in updates.items():
        group[key] = value

    groups[group_name] = group
    save_json(GROUPS_FILE, groups)
    return True, "Group updated."
