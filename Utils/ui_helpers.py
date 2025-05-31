import tkinter as tk

def center_window(window, width=400, height=300):
    """Centers a Tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def clear_frame(frame):
    """Clears all widgets inside a frame."""
    for widget in frame.winfo_children():
        widget.destroy()

def create_label(parent, text, font=None, fg=None, bg=None, pady=5):
    """Creates and packs a label with optional styles."""
    label = tk.Label(parent, text=text, font=font, fg=fg, bg=bg)
    label.pack(pady=pady)
    return label

def create_button(parent, text, command, width=None, pady=5):
    """Creates and packs a button."""
    btn = tk.Button(parent, text=text, command=command, width=width)
    btn.pack(pady=pady)
    return btn

def create_entry(parent, show=None, width=30):
    """Creates and returns an Entry widget."""
    entry = tk.Entry(parent, show=show, width=width)
    entry.pack(pady=5)
    return entry
