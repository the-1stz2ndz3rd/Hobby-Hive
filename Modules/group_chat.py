# modules/group_chat.py
from utils.data_storage import load_json, save_json
import os

GROUP_CHAT_DIR = "data/group_chats"

def get_group_messages(group_name):
    filepath = os.path.join(GROUP_CHAT_DIR, f"{group_name}.json")
    return load_json(filepath)

def add_group_message(group_name, message):
    filepath = os.path.join(GROUP_CHAT_DIR, f"{group_name}.json")
    messages = load_json(filepath)
    if not isinstance(messages, list):
        messages = []
    messages.append(message)
    save_json(filepath, messages)
