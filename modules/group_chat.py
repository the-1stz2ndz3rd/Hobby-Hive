import json
import os
import datetime
import random
from modules.notifications import add_notification
from config import GROUP_DATA_FILE, GROUP_CHAT_DIR, ICEBREAKERS_FILE

# Ensure the directory exists
os.makedirs(GROUP_CHAT_DIR, exist_ok=True)

PREDEFINED_GROUPS = [
    "Music", "Art", "Gaming", "Fitness", "Books",
    "Cooking", "Photography", "Travel", "Tech", "Gardening"
]

def init_groups():
    if not os.path.exists(GROUP_DATA_FILE):
        groups = {name: {"name": name, "members": []} for name in PREDEFINED_GROUPS}
        with open(GROUP_DATA_FILE, "w") as f:
            json.dump(groups, f, indent=2)

def load_groups():
    with open(GROUP_DATA_FILE, "r") as f:
        return json.load(f)

def save_groups(groups):
    with open(GROUP_DATA_FILE, "w") as f:
        json.dump(groups, f, indent=2)

def get_chat_file(group_name):
    safe_name = group_name.replace(" ", "_").lower()
    return os.path.join(GROUP_CHAT_DIR, f"{safe_name}.json")

def load_chat(group_name):
    file = get_chat_file(group_name)
    print("DEBUG: Loading chat from:", file)  # ← 🔧 Add this line
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_chat(group_name, messages):
    file = get_chat_file(group_name)
    with open(file, "w") as f:
        json.dump(messages, f, indent=2)

def get_random_icebreaker():
    try:
        with open(ICEBREAKERS_FILE, "r") as f:
            questions = json.load(f)
        return random.choice(questions) if questions else None
    except:
        return None
def init_groups():
    if not os.path.exists(GROUP_DATA_FILE):
        groups = {}
    else:
        with open(GROUP_DATA_FILE, "r") as f:
            try:
                groups = json.load(f)
            except:
                groups = {}

    # Ensure all predefined groups exist
    for name in PREDEFINED_GROUPS:
        if name not in groups:
            groups[name] = {"name": name, "members": []}

    with open(GROUP_DATA_FILE, "w") as f:
        json.dump(groups, f, indent=2)

def start_group_chat(user):
    print("✅ Entered start_group_chat function.")
    init_groups()
    groups = load_groups()

    # Safety fix: if groups is a list, convert to dict
    if isinstance(groups, list):
        groups = {g["name"]: g for g in groups}
        save_groups(groups)

    user_hobbies = [hobby.lower() for hobby in user.get("hobbies", [])]

    print("User hobbies:", user_hobbies)
    print("Predefined groups:", [g.lower() for g in PREDEFINED_GROUPS])

    available_groups = [g for g in PREDEFINED_GROUPS if g.lower() in user_hobbies]

    if not available_groups:
        print("❌ You have no matching hobby groups. Please update your hobbies.")
        return

    print("\n🌐 Available Groups (based on your hobbies):")
    for i, group_name in enumerate(available_groups, start=1):
        print(f"{i}. {group_name}")

    choice = input("Enter group number to join chat (or 'x' to cancel): ").strip()
    if choice.lower() == 'x':
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(available_groups)):
        print("❌ Invalid selection.")
        return

    selected_group = available_groups[int(choice) - 1]

    # Add user to group if not already there
    if user["username"] not in groups[selected_group]["members"]:
        groups[selected_group]["members"].append(user["username"])
        save_groups(groups)

    messages = load_chat(group_name.lower())

    print(f"\n💬 Entering {selected_group} Group Chat")
    print("Type 'exit' to leave the chat.\n")

    if messages:
        print("📜 Chat History:")
        for msg in messages:
            print(f"[{msg['timestamp']}] {msg['sender']}: {msg['message']}")
    else:
        print("No messages yet.")

    while True:
        msg = input(f"{user['username']}: ").strip()
        if msg.lower() == "exit":
            print("👋 Leaving group chat.")
            break
        if not msg:
            continue

        send_group_message(user, selected_group, msg)

        icebreaker = get_random_icebreaker()
        if icebreaker:
            print(f"\n💡 Icebreaker: {icebreaker}\n")

def send_group_message(sender, group_name, message):
    try:
        with open(GROUP_DATA_FILE, "r") as f:
            groups = json.load(f)
    except:
        print("❌ Could not load group data.")
        return

    # Safety: convert to dict if needed
    if isinstance(groups, list):
        groups = {g["name"]: g for g in groups}

    group_info = groups.get(group_name)
    if not group_info:
        print(f"❌ Group '{group_name}' not found.")
        return

    members = group_info.get("members", [])

    messages = load_chat(group_name)
    messages.append({
        "sender": sender["username"],
        "message": message,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_chat(group_name.lower(), messages)

    for member_username in members:
        if member_username != sender["username"]:
            add_notification(member_username, f"New group message in '{group_name}' from {sender['username']}")
