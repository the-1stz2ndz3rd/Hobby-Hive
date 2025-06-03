import json
import os
from modules.notifications import add_notification
from datetime import datetime
from config import EVENTS_FILE  # Define EVENTS_FILE = "data/events.json" in config.py

# Ensure data directory exists
os.makedirs(os.path.dirname(EVENTS_FILE), exist_ok=True)

def plan_event(user):
    title = input("Event title: ").strip()
    date_str = input("Date (YYYY-MM-DD): ").strip()
    group = input("Associated Group (optional): ").strip()

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format.")
        return

    event = {
        "title": title,
        "date": date_str,
        "creator": user["username"],
        "group": group or None
    }

    try:
        with open(EVENTS_FILE, "r") as f:
            events = json.load(f)
    except:
        events = []

    events.append(event)

    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=2)

    print(f"📅 Event '{title}' on {date_str} created.")
    add_notification(user["username"], f"Event '{title}' created successfully!")

def view_events(user):
    try:
        with open(EVENTS_FILE, "r") as f:
            events = json.load(f)
    except:
        print("📭 No events found.")
        return

    user_events = [e for e in events if e["creator"] == user["username"] or e.get("group") in user.get("hobbies", [])]

    if not user_events:
        print("📭 No upcoming events for you.")
        return

    print("📆 Your Events:")
    for e in user_events:
        print(f"🔸 {e['title']} on {e['date']} (Group: {e['group'] or 'N/A'})")
