import tkinter as tk
from tkinter import scrolledtext
from utils.data_storage import load_json, save_json
import os
import datetime
from PIL import ImageTk, Image

GROUP_CHAT_DIR = "data/group_chats"
GROUP_DATA_FILE = "data/group_data.json"
ICEBREAKER_FILE = "data/icebreakers.json"
CHAT_BG = "assets/backgrounds/group_chat_bg.jpg"

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

def group_chat_screen(root, username, group_name):
    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # Load background image
    try:
        bg_img = Image.open(CHAT_BG)
        bg_img = bg_img.resize((900, 600))
        bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    except:
        pass  # fallback: no bg

    # Load group info
    group_data = load_json(GROUP_DATA_FILE).get(group_name.lower(), {})
    tagline = group_data.get("tagline", "")
    color = group_data.get("color", "#DDFFDD")

    header = tk.Frame(root, bg=color)
    header.pack(fill="x")

    tk.Label(header, text=f"{group_name} 🧑‍🤝‍🧑", font=("Helvetica", 16, "bold"), bg=color).pack()
    tk.Label(header, text=f"“{tagline}”", font=("Helvetica", 10), bg=color).pack()

    # Load and show Icebreaker
    icebreakers = load_json(ICEBREAKER_FILE)
    ice_q = icebreakers.get(group_name.lower(), "What's something you love about this hobby?")
    tk.Label(root, text=f"🔥 Icebreaker: {ice_q}", font=("Helvetica", 10, "italic"), fg="blue").pack(pady=4)

    # Chat display
    chat_display = scrolledtext.ScrolledText(root, width=90, height=20, state="disabled", wrap="word", font=("Helvetica", 11))
    chat_display.pack(pady=10)

    def load_messages():
        chat_display.configure(state="normal")
        chat_display.delete("1.0", tk.END)
        messages = get_group_messages(group_name)
        for msg in messages:
            sender = msg.get("sender")
            time = msg.get("timestamp")
            content = msg.get("content")
            line = f"[{time}] {sender}: {content}\n"
            chat_display.insert(tk.END, line)
        chat_display.configure(state="disabled")

    load_messages()

    # Message entry
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    msg_entry = tk.Entry(input_frame, width=70)
    msg_entry.pack(side="left", padx=5)

    def send_message():
        content = msg_entry.get().strip()
        if content:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            msg = {"sender": username, "timestamp": timestamp, "content": content}
            add_group_message(group_name, msg)
            load_messages()
            msg_entry.delete(0, tk.END)

    send_btn = tk.Button(input_frame, text="Send", command=send_message)
    send_btn.pack(side="right", padx=5)

    # Back to dashboard button
    tk.Button(root, text="Back", command=lambda: __import__('modules.user_profiles').user_profiles.dashboard_screen(root, username)).pack(pady=5)
