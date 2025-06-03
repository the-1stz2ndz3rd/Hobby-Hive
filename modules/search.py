import json
from config import USER_DATA_FILE  # Make sure this is correctly defined

def search_users():
    query = input("Search by hobby or name: ").strip().lower()

    try:
        with open(USER_DATA_FILE, "r") as f:
            users = json.load(f)
    except:
        print("❌ Could not load user data.")
        return

    matches = []
    for user in users:
        name = user["username"].lower()
        hobbies = [h.lower() for h in user.get("hobbies", [])]
        if query in name or any(query in hobby for hobby in hobbies):
            matches.append(user)

    if not matches:
        print("📭 No users found.")
        return

    print(f"\n🔍 Results for '{query}':")
    for user in matches:
        print(f"👤 {user['username']} | Hobbies: {', '.join(user['hobbies'])}")
