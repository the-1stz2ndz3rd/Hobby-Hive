from users_data import users
from matching import display_matches
from search import search_users
from private_chat import display_private_chat_ui

def main():
    current_user = input("Enter your username: ").strip()
    if current_user not in users:
        print("User not found.")
        return

    while True:
        print("\n--- Menu ---")
        print("1. Search Users")
        print("2. View Matches")
        print("3. Chat with a user")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            query = input("Enter name or hobby to search: ")
            results = search_users(query)
            print("Results:", results)
        elif choice == "2":
            display_matches(current_user)
        elif choice == "3":
            partner = input("Enter username to chat with: ")
            if partner in users:
                display_private_chat_ui(current_user, partner)
            else:
                print("User not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
