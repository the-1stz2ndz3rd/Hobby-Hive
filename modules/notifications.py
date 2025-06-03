import json
import os
from config import NOTIFICATIONS_FILE  # e.g. "data/notifications.json"

# Make sure the directory exists
os.makedirs(os.path.dirname(NOTIFICATIONS_FILE), exist_ok=True)

def show_notifications(user):
    """
    Show all notifications for the given user.
    """
    try:
        with open(NOTIFICATIONS_FILE, "r") as f:
            notifications = json.load(f)
    except FileNotFoundError:
        notifications = {}

    user_notes = notifications.get(user["username"], [])

    if not user_notes:
        print("📭 You have no new notifications.")
        return

    print(f"🔔 Notifications for {user['username']}:")
    for i, note in enumerate(user_notes, 1):
        print(f"{i}. {note}")

    # Optionally clear notifications after showing
    clear = input("Clear notifications? (y/n): ").strip().lower()
    if clear == 'y':
        notifications[user["username"]] = []
        with open(NOTIFICATIONS_FILE, "w") as f:
            json.dump(notifications, f, indent=2)
        print("✅ Notifications cleared.")

def add_notification(username, message):
    """
    Add a notification message to the specified username.
    """
    try:
        with open(NOTIFICATIONS_FILE, "r") as f:
            notifications = json.load(f)
    except FileNotFoundError:
        notifications = {}

    notifications.setdefault(username, []).append(message)

    with open(NOTIFICATIONS_FILE, "w") as f:
        json.dump(notifications, f, indent=2)
