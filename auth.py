import json
import os

USER_DATA_FILE = "users.json"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_user_data(user_data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_data, file, indent=4)

def sign_up():
    user_data = load_user_data()

    print("=== Sign Up ===")
    full_name = input("Full Name: ")
    student_id = input("Student ID: ")
    username = input("Choose a username: ")

    if username in user_data:
        print("⚠️ Username already exists. Please try logging in.")
        return None

    password = input("Choose a password: ")

    hobbies = input("Enter your hobbies (separate by commas): ").split(",")
    hobbies = [h.strip().capitalize() for h in hobbies]

    bio = input("Write a short bio/status: ")

    user = {
        "full_name": full_name,
        "student_id": student_id,
        "username": username,
        "password": password,  # Plain text for now
        "hobbies": hobbies,
        "bio": bio
    }

    user_data[username] = user
    save_user_data(user_data)

    print(f"✅ Welcome, {full_name}! You've been signed up successfully.\n")
    return user

def log_in():
    user_data = load_user_data()

    print("=== Log In ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in user_data and user_data[username]["password"] == password:
        print("✅ Login successful!\n")
        return user_data[username]
    else:
        print("❌ Incorrect username or password.\n")
        return None
