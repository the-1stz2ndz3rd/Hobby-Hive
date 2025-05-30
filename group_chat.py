# group_chat.py

import os
import json
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext

CHAT_DIR = "HobbyHive/data/group_chats"
ICEBREAKER_FILE = "HobbyHive/data/icebreakers.json"

# Ensure the chat directory exists
os.makedirs(CHAT_DIR, exist_ok=True)

def load_group_chat(group_name):
    """Loads chat messages for a specific group."""
    filepath = os.path.join(CHAT_DIR, f"{group_name}_chat.txt")
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as file:
        return file.readlines()

def save_group_message(group_name, message):
    """Appends a new message to the group chat file."""
    filepath = os.path.join(CHAT_DIR, f"{group_name}_chat.txt")
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(message + "\n")

def generate_icebreaker(group_name):
    """Selects a random icebreaker for the group."""
    if not os.path.exists(ICEBREAKER_FILE):
        return "What's one reason you enjoy this hobby?"
    with open(ICEBREAKER_FILE, "r", encoding="utf-8") as file:
        icebreakers = json.load(file)
    return random.choice(icebreakers.get(group_name, ["What's your favorite thing about this hobby?"]))

def display_group_chat_ui(group_name):
    """Displays the UI for a group chat."""
    root = tk.Tk()
    root.title(f"{group_name} Chat Room")
    root.geometry("500x600")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text=f"{group_name} Group Chat", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(root, text=generate_icebreaker(group_name), font=("Helvetica", 10, "italic"), fg="blue").pack(pady=5)

    chat_display = scrolledtext.ScrolledText(root, width=60, height=25, state="disabled")
    chat_display.pack(padx=10, pady=10)

    def refresh_chat():
        chat_display.config(state="normal")
        chat_display.delete(1.0, tk.END)
        messages = load_group_chat(group_name)
        for msg in messages:
            chat_display.insert(tk.END, msg)
        chat_display.config(state="disabled")

    def send_message():
        msg = message_entry.get()
        if msg.strip():
            formatted_msg = f"You: {msg}"
            save_group_message(group_name, formatted_msg)
            message_entry.delete(0, tk.END)
            refresh_chat()
        else:
            messagebox.showwarning("Empty Message", "Please enter a message before sending.")

    refresh_chat()

    message_entry = tk.Entry(root, width=40)
    message_entry.pack(side="left", padx=(10, 5), pady=10)

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(side="left", pady=10)

    root.mainloop()
