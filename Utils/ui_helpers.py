# utils/ui_helpers.py

import tkinter as tk
from utils.themes import get_current_theme


def center_window(window, width=900, height=600):
    """Centers a Tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def clear_frame(frame):
    """Removes all widgets inside a frame."""
    for widget in frame.winfo_children():
        widget.destroy()


def create_label(parent, text, font=("Helvetica", 12), pady=5):
    """Creates and returns a label with theme support."""
    theme = get_current_theme()
    label = tk.Label(parent, text=text, font=font, fg=theme["fg"], bg=theme["bg"])
    label.pack(pady=pady)
    return label


def create_button(parent, text, command, width=20, pady=5, icon_path=None):
    """Creates a themed button. Optional icon support."""
    theme = get_current_theme()
    btn = tk.Button(parent, text=text, command=command, width=width, bg=theme["button_bg"], fg=theme["fg"])

    # If icon is provided (e.g., assets/icons/login.png)
    if icon_path:
        icon = tk.PhotoImage(file=icon_path)
        btn.config(image=icon, compound="left")
        btn.image = icon  # prevent garbage collection

    btn.pack(pady=pady)
    return btn


def create_entry(parent, show=None, width=30):
    """Creates a themed Entry widget."""
    theme = get_current_theme()
    entry = tk.Entry(parent, show=show, width=width, bg=theme["entry_bg"], fg=theme["fg"])
    entry.pack(pady=5)
    return entry
