from config import DARK_MODE

def toggle_dark_mode(user):
    DARK_MODE["enabled"] = not DARK_MODE["enabled"]
    mode = "Dark" if DARK_MODE["enabled"] else "Light"
    print(f"🌓 Switched to {mode} mode.")