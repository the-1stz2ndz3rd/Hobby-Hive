# modules/moderator_tools.py
from utils.data_storage import load_json, save_json

USERS_FILE = "data/users_data.json"
GROUP_CHATS_DIR = "data/group_chats/"

def warn_user(username, reason):
    users = load_json(USERS_FILE)
    if username in users:
        warnings = users[username].get("warnings", [])
        warnings.append(reason)
        users[username]["warnings"] = warnings
        save_json(USERS_FILE, users)
        return True
    return False

def kick_user_from_group(username, group_name):
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
    chat_file = f"{GROUP_CHATS_DIR}{group_name}.json"
    messages = load_json(chat_file)
    if not messages:
        return False
    filtered = [msg for msg in messages if msg.get("id") != message_id]
    save_json(chat_file, filtered)
    return True
