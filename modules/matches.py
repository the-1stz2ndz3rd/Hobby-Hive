import json
from config import USER_DATA_FILE
from modules.notifications import add_notification

def find_matches(current_user):
    print(f"\n🔗 Finding matches for {current_user['username']}...")
    try:
        with open(USER_DATA_FILE, 'r') as f:
            all_users = json.load(f)
    except:
        all_users = []

    my_hobbies = set(h.strip().lower() for h in current_user.get("hobbies", []))
    matches = []

    for user in all_users:
        if user["username"] == current_user["username"]:
            continue
        their_hobbies = set(h.strip().lower() for h in user.get("hobbies", []))
        common = my_hobbies & their_hobbies
        if len(common) >= 2:
            matches.append({
                "username": user["username"],
                "common_hobbies": list(common),
                "total_common": len(common)
            })

    if not matches:
        print("😔 No matches found with 2+ hobbies in common.")
        return

    # Display sorted matches by number of common hobbies
    matches.sort(key=lambda x: x["total_common"], reverse=True)
    print("🎯 Matches found:")
    for idx, match in enumerate(matches, 1):
        print(f"  {idx}. {match['username']} | Common hobbies: {', '.join(match['common_hobbies'])}")

    # Optional: Let user choose someone to chat with
    choice = input("\n💬 Do you want to start a private chat with a match? Enter number or press Enter to skip: ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(matches):
            from modules.private_chat import start_private_chat
            target_user = matches[index]["username"]

            # Load full user info from the file
            for u in all_users:
                if u["username"] == target_user:
                    matched_user_obj = u
                    break
            else:
                print("⚠️ Error: Matched user not found.")
                return

            print(f"💌 Starting private chat with {target_user}...")
            start_private_chat(current_user, matched_user_obj)
        else:
            print("⚠️ Invalid match number.")
    # ... existing matching code ...

    for match_user in matches:
        add_notification(match_user["username"], f"You have a new match with {current_user['username']}!")
        add_notification(current_user["username"], "You have new matches!")
