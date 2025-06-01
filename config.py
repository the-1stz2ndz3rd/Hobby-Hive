# config.py

# === App Identity ===
APP_TITLE = "🐝 HobbyHive"
APP_NAME = "HobbyHive"

# === Data Paths ===
DATA_DIR = "data"
GROUP_CHATS_DIR = f"{DATA_DIR}/group_chats"
PRIVATE_CHATS_DIR = f"{DATA_DIR}/private_chats"

USERS_FILE = f"{DATA_DIR}/users_data.json"
GROUP_DATA_FILE = f"{DATA_DIR}/group_data.json"
ICEBREAKERS_FILE = f"{DATA_DIR}/icebreakers.json"
EVENTS_FILE = f"{DATA_DIR}/events.json"
POLLS_FILE = f"{DATA_DIR}/polls.json"
NOTIFICATIONS_FILE = f"{DATA_DIR}/notifications.json"
SETTINGS_FILE = f"{DATA_DIR}/settings.json"

# === UI Dimensions ===
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# === UI Themes (Light/Dark Mode) ===
THEME_LIGHT = {
    "bg": "#FFFFFF",
    "fg": "#000000",
    "button_bg": "#E0F7FA",
    "entry_bg": "#F0F0F0",
    "highlight": "#90CAF9"
}

THEME_DARK = {
    "bg": "#2E2E2E",
    "fg": "#FFFFFF",
    "button_bg": "#424242",
    "entry_bg": "#383838",
    "highlight": "#64B5F6"
}

# === Icons and Visual Assets ===
ASSETS_DIR = "assets"
ICONS_DIR = f"{ASSETS_DIR}/icons"
BACKGROUNDS_DIR = f"{ASSETS_DIR}/backgrounds"
GROUP_IMAGES_DIR = f"{ASSETS_DIR}/group_images"
