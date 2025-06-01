# modules/event_planning.py

import os
from datetime import datetime
from utils.data_storage import load_json, save_json

EVENTS_FILE = "data/events.json"

def get_events():
    """
    Load and return all scheduled events as a list of dictionaries.
    Each event contains: title, group, datetime, description, created_by
    """
    events = load_json(EVENTS_FILE)
    return events if isinstance(events, list) else []

def add_event(event):
    """
    Adds a new event.
    Expected event dict keys:
        - title (str)
        - group (str): e.g. "Hiking"
        - datetime (ISO format str): "2025-06-01T14:30:00"
        - description (str)
        - created_by (username)
    """
    required_keys = {"title", "group", "datetime", "description", "created_by"}
    if not isinstance(event, dict) or not required_keys.issubset(event):
        return False, "Invalid event format."

    # Validate datetime format
    try:
        datetime.fromisoformat(event["datetime"])
    except ValueError:
        return False, "Invalid datetime format. Use ISO format."

    events = get_events()
    events.append(event)
    save_json(EVENTS_FILE, events)
    return True, "Event created successfully."

def get_group_events(group_name):
    """
    Return only the events associated with a specific group
    """
    events = get_events()
    return [e for e in events if e.get("group") == group_name]

def delete_event(index):
    """
    Delete event by index in the list. (e.g. for moderator access)
    """
    events = get_events()
    if 0 <= index < len(events):
        deleted = events.pop(index)
        save_json(EVENTS_FILE, events)
        return True, f"Deleted event: {deleted.get('title')}"
    return False, "Invalid index for deletion."
