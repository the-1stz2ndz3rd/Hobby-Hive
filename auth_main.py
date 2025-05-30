# auth_main.py
from auth import sign_up, log_in
from profile import display_profile

def main():
    print("🎉 Welcome to Hobby Hive 🎉")
    choice = input("Do you want to (1) Sign Up or (2) Log In? Enter 1 or 2: ")

    if choice == "1":
        user = sign_up()
    elif choice == "2":
        user = log_in()
    else:
        print("Invalid choice.")
        return

    if user:
        display_profile(user)

if __name__ == "__main__":
    main()
