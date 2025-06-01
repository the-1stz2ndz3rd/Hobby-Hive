# utils/ui_helpers.py
import tkinter as tk
from PIL import Image, ImageTk
from config import ICONS_DIR
from themes import get_theme_colors

def center_window(window, width=400, height=300):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def create_label(parent, text, font=None, pady=5):
    bg, fg = get_theme_colors()
    label = tk.Label(parent, text=text, font=font, bg=bg, fg=fg)
    label.pack(pady=pady)
    return label

def create_button(parent, text, command=None, width=20, icon=None, pady=5):
    bg, fg = get_theme_colors()
    if icon:
        icon_path = f"{ICONS_DIR}/{icon}"
        icon_img = Image.open(icon_path).resize((18, 18))
        icon_photo = ImageTk.PhotoImage(icon_img)
        btn = tk.Button(parent, text=text, image=icon_photo, compound="left", command=command,
                        width=width, bg=bg, fg=fg)
        btn.image = icon_photo  # Keep reference!
    else:
        btn = tk.Button(parent, text=text, command=command, width=width, bg=bg, fg=fg)
    btn.pack(pady=pady)
    return btn

def create_entry(parent, show=None, width=30):
    bg, fg = get_theme_colors()
    entry = tk.Entry(parent, show=show, width=width, bg=bg, fg=fg)
    entry.pack(pady=5)
    return entry
