# modules/settings.py
from utils.data_storage import load_json, save_json

SETTINGS_FILE = "data/settings.json"

def get_settings():
    settings = load_json(SETTINGS_FILE)
    if not settings:
        settings = {"dark_mode": False}
    return settings

def toggle_dark_mode():
    settings = get_settings()
    settings["dark_mode"] = not settings.get("dark_mode", False)
    save_json(SETTINGS_FILE, settings)
    return settings["dark_mode"]
