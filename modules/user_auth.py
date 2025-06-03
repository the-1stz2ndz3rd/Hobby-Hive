import json
from config import USER_DATA_FILE
from modules.notifications import show_notifications

def sign_up():
    username = input("Username: ")
    password = input("Password: ")
    hobbies = input("Enter hobbies (comma-separated): ").split(",")
    clean_hobbies = [h.strip().lower() for h in hobbies]
    user = {"username": username, "password": password, "hobbies": clean_hobbies}

    
    try:
        with open(USER_DATA_FILE, "r") as f:
            users = json.load(f)
    except:
        users = []
    
    from modules.notifications import add_notification
    for existing_user in users:
        existing_hobbies = set(h.strip().lower() for h in existing_user.get("hobbies", []))
        input_hobbies = set(h.strip().lower() for h in hobbies)
        common = existing_hobbies & set(hobbies)
        if len(common) >= 2:
            add_notification(existing_user["username"], f"New user '{username}' matches your hobbies!")
            add_notification(username, f"You matched with '{existing_user['username']}'!")
        
    users.append(user)
    
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)
        
    print("✅ Signed up successfully.")
    return user

def login():
    username = input("Username: ")
    password = input("Password: ")
    try:
        with open(USER_DATA_FILE, "r") as f:
            users = json.load(f)
    except:
        print("❌ No user data found.")
        return None
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("✅ Login successful.")
            show_notifications(user)
            return user
    print("❌ Login failed.")
    return None

def load_users():
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

