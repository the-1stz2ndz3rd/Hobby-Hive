# Define color schemes for light and dark modes

LIGHT_THEME = {
    "bg": "#ffffff",
    "fg": "#000000",
    "button_bg": "#e0e0e0",
    "button_fg": "#000000",
    "entry_bg": "#f9f9f9",
    "entry_fg": "#000000",
    "highlight": "#007acc"
}

DARK_THEME = {
    "bg": "#2e2e2e",
    "fg": "#f5f5f5",
    "button_bg": "#444444",
    "button_fg": "#f5f5f5",
    "entry_bg": "#3a3a3a",
    "entry_fg": "#f5f5f5",
    "highlight": "#1e90ff"
}

def apply_theme(widget, theme):
    """
    Recursively applies theme colors to widget and its children.
    widget: any Tkinter widget (Frame, Label, Button, etc.)
    theme: dict containing color values
    """
    try:
        widget.configure(bg=theme["bg"], fg=theme.get("fg", ""))
    except:
        # Some widgets (e.g. Frame) don't have fg option
        try:
            widget.configure(bg=theme["bg"])
        except:
            pass

    # Special handling for some widgets
    if isinstance(widget, (tk.Button, tk.Entry)):
        widget.configure(
            bg=theme.get("button_bg", theme["bg"]),
            fg=theme.get("button_fg", theme.get("fg", "")),
            insertbackground=theme.get("fg", "#000")
        )
        if isinstance(widget, tk.Entry):
            widget.configure(
                bg=theme.get("entry_bg", theme["bg"]),
                fg=theme.get("entry_fg", theme.get("fg", ""))
            )

    # Recursively apply theme to children widgets
    for child in widget.winfo_children():
        apply_theme(child, theme)
