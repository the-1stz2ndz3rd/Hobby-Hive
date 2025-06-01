 # modules/moderator_tools.py

import os
from utils.data_storage import load_json, save_json

USERS_FILE = "data/users_data.json"
GROUP_CHATS_DIR = "data/group_chats"

def warn_user(username, reason):
    """
    Add a warning to a user with a reason.
    Returns True if successful.
    """
    users = load_json(USERS_FILE)
    if username in users:
        users[username].setdefault("warnings", []).append(reason)
        save_json(USERS_FILE, users)
        return True
    return False

def kick_user_from_group(username, group_name):
    """
    Remove user from a hobby group.
    Returns True if successful.
    """
    users = load_json(USERS_FILE)
    if username in users:
        groups = users[username].get("groups", [])
        if group_name in groups:
            groups.remove(group_name)
            users[username]["groups"] = groups
            save_json(USERS_FILE, users)
            return True
    return False

def delete_message(group_name, message_id):
    """
    Delete a message by ID in a group chat.
    Returns True if deleted, False otherwise.
    """
    filepath = os.path.join(GROUP_CHATS_DIR, f"{group_name}.json")
    messages = load_json(filepath)

    if not isinstance(messages, list):
        return False

    updated_messages = [msg for msg in messages if msg.get("id") != message_id]

    if len(updated_messages) == len(messages):
        return False  # No message was deleted (ID not found)

    save_json(filepath, updated_messages)
    return True

def edit_pinned_message(group_name, new_pinned_text):
    """
    Update the pinned message for a group.
    """
    group_data_path = "data/group_data.json"
    groups = load_json(group_data_path)

    if group_name in groups:
        groups[group_name]["pinned_message"] = new_pinned_text
        save_json(group_data_path, groups)
        return True
    return False
