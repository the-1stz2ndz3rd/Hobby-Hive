# modules/notifications.py
from utils.data_storage import load_json, save_json

NOTIFICATIONS_FILE = "data/notifications.json"


def get_notifications(username):
    notifications = load_json(NOTIFICATIONS_FILE)
    if not isinstance(notifications, dict):
        notifications = {}
    return notifications.get(username, [])

def add_notification(username, notification):
    notifications = load_json(NOTIFICATIONS_FILE)
    if not isinstance(notifications, dict):
        notifications = {}
    user_notes = notifications.get(username, [])
    user_notes.append(notification)
    notifications[username] = user_notes
    save_json(NOTIFICATIONS_FILE, notifications)

def clear_notifications(username):
    notifications = load_json(NOTIFICATIONS_FILE)
    if not isinstance(notifications, dict):
        notifications = {}
    if username in notifications:
        notifications[username] = []
        save_json(NOTIFICATIONS_FILE, notifications)
