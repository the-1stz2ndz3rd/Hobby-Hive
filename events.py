# events.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

events_dir = "events"
if not os.path.exists(events_dir):
    os.makedirs(events_dir)

def create_event(group_name):
    event_title = simpledialog.askstring("Event Title", "Enter event title:")
    event_time = simpledialog.askstring("Date & Time", "Enter date and time (e.g. 2025-05-30 10:00):")
    event_desc = simpledialog.askstring("Description", "Enter event description:")

    if not (event_title and event_time and event_desc):
        messagebox.showwarning("Incomplete", "All fields are required.")
        return

    event_data = {
        "title": event_title,
        "datetime": event_time,
        "description": event_desc
    }

    file_path = os.path.join(events_dir, f"{group_name}_events.json")
    events = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                events = json.load(f)
            except json.JSONDecodeError:
                events = []

    events.append(event_data)

    with open(file_path, "w") as f:
        json.dump(events, f, indent=2)

    messagebox.showinfo("Success", "Event created successfully!")

def load_events(group_name):
    file_path = os.path.join(events_dir, f"{group_name}_events.json")
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def display_events(group_name):
    events = load_events(group_name)
    win = tk.Toplevel()
    win.title(f"{group_name} Events")

    if not events:
        tk.Label(win, text="No events yet.", pady=10).pack()
        return

    for event in events:
        event_str = f"{event['title']}\n{event['datetime']}\n{event['description']}\n"
        tk.Label(win, text=event_str, justify="left", anchor="w", padx=10, pady=10).pack(fill='x')




