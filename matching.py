from users_data import users

def find_matches(current_user):
    matches = []
    user_hobbies = set(users[current_user]["hobbies"])
    for user, data in users.items():
        if user == current_user or user in users[current_user]["blocked"]:
            continue
        shared = user_hobbies.intersection(data["hobbies"])
        if len(shared) >= 2:
            matches.append((user, shared))
    return matches

def display_matches(current_user):
    matches = find_matches(current_user)
    print(f"\n--- Matches for {current_user} ---")
    for user, shared in matches:
        print(f"{user} (shared hobbies: {', '.join(shared)})")
        print("1. Message")
        print("2. Block")
        choice = input("Choose an option (1-2 or skip): ")
        if choice == "1":
            from private_chat import display_private_chat_ui
            display_private_chat_ui(current_user, user)
        elif choice == "2":
            users[current_user]["blocked"].append(user)
            print(f"{user} has been blocked.")
