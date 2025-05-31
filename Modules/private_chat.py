# modules/private_chat.py
from utils.data_storage import load_json, save_json
import os

PRIVATE_CHAT_DIR = "data/private_chats"

def _chat_filename(user1, user2):
    """Return consistent filename for private chat between two users"""
    sorted_users = sorted([user1, user2])
    return f"{sorted_users[0]}_{sorted_users[1]}.json"

def get_private_messages(user1, user2):
    filename = _chat_filename(user1, user2)
    filepath = os.path.join(PRIVATE_CHAT_DIR, filename)
    return load_json(filepath)

def add_private_message(user1, user2, message):
    filename = _chat_filename(user1, user2)
    filepath = os.path.join(PRIVATE_CHAT_DIR, filename)
    messages = load_json(filepath)
    if not isinstance(messages, list):
        messages = []
    messages.append(message)
    save_json(filepath, messages)
