import json
import os
import datetime
import random
from config import PRIVATE_CHAT_DIR, ICEBREAKERS_FILE
from modules.notifications import add_notification

# Ensure chat directory exists
os.makedirs(PRIVATE_CHAT_DIR, exist_ok=True)

def get_chat_filename(user1, user2):
    sorted_users = sorted([user1["username"], user2["username"]])
    return os.path.join(PRIVATE_CHAT_DIR, f"{sorted_users[0]}_{sorted_users[1]}.json")

def load_chat_history(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_chat_history(filename, history):
    with open(filename, "w") as f:
        json.dump(history, f, indent=2)

def get_random_icebreaker():
    try:
        with open(ICEBREAKERS_FILE, "r") as f:
            icebreakers = json.load(f)
        return random.choice(icebreakers) if icebreakers else None
    except:
        return None

def start_private_chat(user1, user2=None):
    if not user2:
        # Prompt to enter a username
        target_username = input("Enter the username of the person you want to chat with: ").strip()
        from modules.user_auth import load_users
        all_users = load_users()
        for u in all_users:
            if u["username"] == target_username:
                user2 = u
                break
        else:
            print("❌ User not found.")
            return

    if user1["username"] == user2["username"]:
        print("⚠️ You can't chat with yourself!")
        return

    chat_file = get_chat_filename(user1, user2)
    history = load_chat_history(chat_file)

    print(f"\n💬 Private Chat between {user1['username']} and {user2['username']}")
    print("Type 'exit' to leave the chat.\n")

    # Show previous messages
    if history:
        print("📜 Previous Messages:")
        for msg in history:
            ts = msg['timestamp']
            print(f"[{ts}] {msg['sender']}: {msg['message']}")
    else:
        print("No previous messages.")

    while True:
        msg = input(f"{user1['username']}: ").strip()
        if msg.lower() == "exit":
            print("👋 Leaving chat.")
            break
        if msg == "":
            continue
        send_private_message(user1, user2["username"], msg)

        # Display icebreaker after each message
        icebreaker = get_random_icebreaker()
        if icebreaker:
            print(f"\n💡 Icebreaker: {icebreaker}\n")
def send_private_message(sender, recipient_username, message):
    # ... existing code to send message ...

    # Notify recipient
    add_notification(recipient_username, f"New message from {sender['username']}")

