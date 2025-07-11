from modules.user_auth import sign_up, login
from modules.user_profiles import setup_profile
from modules.private_chat import start_private_chat 
from modules.event_planning import plan_event, view_events
from modules.matches import find_matches
from modules.group_chat import start_group_chat
from modules.notifications import show_notifications
from modules.moderator_tools import moderator_panel
from modules.polls import create_poll, vote_in_poll, view_poll_results
from modules.search import search_users
from modules.setting import toggle_dark_mode
from modules.group_management import assign_groups
from modules.users import view_profile
from modules import user_auth 


def main():
    init_data()
    print("🧩 Welcome to HobbyHive!")
    while True:
        print("\n1. Sign Up\n2. Log In\n3. Exit")
        choice = input("Select option: ")
        if choice == '1':
            user = sign_up()
            setup_profile(user)
        elif choice == '2':
            user = login()
            if user:
                view_events(user)
                input("\npress Enter to continue to dashboard...")  # Show their events first
                dashboard(user)    # Then go to dashboard

        elif choice == '3':
            break

def dashboard(user):
    assign_groups(user)
    while True:
        print(f"\n📋 Dashboard for {user['username']}")
        print("1. Group Chat\n2. Private Chat\n3. Plan/View Events\n4. Matches\n5. View Profile\n6. Search Users\n7. Polls")
        print("8. Notifications\n9. Moderator Tools\n10. Dark Mode\n11. Logout")
        choice = input("Choose action: ").strip()
        print(f"DEBUG: Raw input was: { repr(choice)}")

        if choice == '1':
            print("DEBUG: You selected group chat.")
            print("DEBUG: start_group_chat was called.")
            start_group_chat(user)
        elif choice == '2':
            start_private_chat(user)
        elif choice == '3':
            while True:
                print("\n📅 Event Menu:")
                print("1. Plan Event")
                print("2. View Events")
                print("3. Back to Dashboard")
                event_choice = input("Choose option: ").strip()
                if event_choice == '1':
                    plan_event(user)
                elif event_choice == '2':
                    view_events(user)
                elif event_choice == '3':
                    break
                else:
                    print("❌ Invalid choice, try again.")
        elif choice == '4':
            find_matches(user)
        elif choice == '5':
            view_profile(user)
        elif choice == '6':
            search_users()
        elif choice == '7':
            while True:
                print("\n📊 Poll Menu:")
                print("1. Create Poll")
                print("2. Vote in Poll")
                print("3. View Poll Results")
                print("4. Back to Dashboard")
                poll_choice = input("Choose option: ").strip()
                if poll_choice == '1':
                    create_poll(user)
                elif poll_choice == '2':
                    vote_in_poll(user)
                elif poll_choice == '3':
                    view_poll_results()
                elif poll_choice == '4':
                    break
                else:
                     print("❌ Invalid choice.")

        elif choice == '8':
            show_notifications(user)
        elif choice == '9':
            moderator_panel()
        elif choice == '10':
            toggle_dark_mode(user)
        elif choice == '11':
            break

if __name__ == "__main__":
    main()
