# modules/private_chat.py

import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import datetime

from utils.data_storage import load_json, save_json
from utils.ui_helpers import style_chat_bubble
from utils.themes import get_current_theme
from data.icebreakers import get_random_icebreaker

PRIVATE_CHAT_DIR = "data/private_chats"

def _chat_filename(user1, user2):
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

def private_chat_screen(root, current_user, other_user):
    """Render 1-on-1 private chat UI"""
    root.title(f"Chat with {other_user}")
    for widget in root.winfo_children():
        widget.destroy()

    theme = get_current_theme()

    # Icebreaker popup
    messagebox.showinfo("Icebreaker", get_random_icebreaker())

    # Header
    header = tk.Label(root, text=f"Chat with {other_user}", font=("Helvetica", 16, "bold"))
    header.pack(pady=10)

    # Chat window
    chat_frame = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled', wrap=tk.WORD)
    chat_frame.pack(pady=10)

    def load_messages():
        chat_frame.config(state='normal')
        chat_frame.delete('1.0', tk.END)
        messages = get_private_messages(current_user, other_user)
        if isinstance(messages, list):
            for msg in messages:
                sender = msg['sender']
                timestamp = msg['timestamp']
                content = msg['content']
                align = 'right' if sender == current_user else 'left'
                style_chat_bubble(chat_frame, sender, content, timestamp, align)
        chat_frame.config(state='disabled')

    load_messages()

    # Message entry
    input_frame = tk.Frame(root)
    input_frame.pack(pady=5)

    entry = tk.Entry(input_frame, width=60)
    entry.pack(side=tk.LEFT, padx=5)

    def send_message():
        content = entry.get().strip()
        if not content:
            return
        timestamp = datetime.datetime.utcnow().isoformat()
        message = {"sender": current_user, "timestamp": timestamp, "content": content}
        add_private_message(current_user, other_user, message)
        entry.delete(0, tk.END)
        load_messages()

    send_btn = tk.Button(input_frame, text="Send", command=send_message)
    send_btn.pack(side=tk.LEFT)

    # Block & Report
    options_frame = tk.Frame(root)
    options_frame.pack(pady=10)

    tk.Button(options_frame, text="🚫 Block", command=lambda: messagebox.showinfo("Blocked", f"You blocked {other_user}")).pack(side=tk.LEFT, padx=5)
    tk.Button(options_frame, text="⚠️ Report", command=lambda: messagebox.showinfo("Reported", f"You reported {other_user}")).pack(side=tk.LEFT, padx=5)

