import tkinter as tk
from tkinter import messagebox
from utils.validation import is_valid_signup, is_valid_login
from utils.data_storage import load_json, save_json

USERS_FILE = "data/users_data.json"

def signup(user_data):
    users = load_json(USERS_FILE)
    if user_data["username"] in users:
        return False, "Username already exists."
    valid, msg = is_valid_signup(user_data)
    if not valid:
        return False, msg
    users[user_data["username"]] = user_data
    save_json(USERS_FILE, users)
    return True, "Account created successfully."

def login(username, password):
    users = load_json(USERS_FILE)
    valid, msg = is_valid_login(username, password)
    if not valid:
        return False, msg
    if username not in users or users[username]["password"] != password:
        return False, "Invalid username or password."
    return True, "Login successful."

def login_screen(root, on_success, on_back):
    """Display login form in root. Call on_success(username) on success, on_back() to go back."""
    frame = tk.Frame(root)
    frame.pack(pady=20)

    tk.Label(frame, text="Username:").grid(row=0, column=0, sticky="e")
    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1)

    tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="e")
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1)

    def submit():
        username = username_entry.get().strip()
        password = password_entry.get()
        success, msg = login(username, password)
        if success:
            messagebox.showinfo("Success", msg)
            on_success(username)
        else:
            messagebox.showerror("Error", msg)

    login_btn = tk.Button(frame, text="Log In", command=submit)
    login_btn.grid(row=2, column=0, columnspan=2, pady=10)

    back_btn = tk.Button(frame, text="Back", command=lambda: [frame.destroy(), on_back()])
    back_btn.grid(row=3, column=0, columnspan=2)

def signup_screen(root, on_success, on_back):
    """Display signup form in root. Call on_success(username) on success, on_back() to go back."""
    frame = tk.Frame(root)
    frame.pack(pady=20)

    tk.Label(frame, text="Full Name:").grid(row=0, column=0, sticky="e")
    name_entry = tk.Entry(frame)
    name_entry.grid(row=0, column=1)

    tk.Label(frame, text="Student ID:").grid(row=1, column=0, sticky="e")
    student_id_entry = tk.Entry(frame)
    student_id_entry.grid(row=1, column=1)

    tk.Label(frame, text="Username:").grid(row=2, column=0, sticky="e")
    username_entry = tk.Entry(frame)
    username_entry.grid(row=2, column=1)

    tk.Label(frame, text="Password:").grid(row=3, column=0, sticky="e")
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=3, column=1)

    tk.Label(frame, text="Bio/Status:").grid(row=4, column=0, sticky="e")
    bio_entry = tk.Entry(frame)
    bio_entry.grid(row=4, column=1)

    # Hobby checkboxes
    hobbies_list = ["Art", "Hiking", "Music", "Photography", "Reading"]  # expand as needed
    hobbies_vars = {}
    tk.Label(frame, text="Select Hobbies:").grid(row=5, column=0, sticky="ne")
    hobbies_frame = tk.Frame(frame)
    hobbies_frame.grid(row=5, column=1, sticky="w")
    for i, hobby in enumerate(hobbies_list):
        var = tk.BooleanVar()
        cb = tk.Checkbutton(hobbies_frame, text=hobby, variable=var)
        cb.grid(row=i // 2, column=i % 2, sticky="w")
        hobbies_vars[hobby] = var

    def submit():
        user_data = {
            "name": name_entry.get().strip(),
            "student_id": student_id_entry.get().strip(),
            "username": username_entry.get().strip(),
            "password": password_entry.get(),
            "bio": bio_entry.get().strip(),
            "hobbies": [h for h, v in hobbies_vars.items() if v.get()]
        }
        success, msg = signup(user_data)
        if success:
            messagebox.showinfo("Success", msg)
            on_success(user_data["username"])
        else:
            messagebox.showerror("Error", msg)

    signup_btn = tk.Button(frame, text="Create Account", command=submit)
    signup_btn.grid(row=6, column=0, columnspan=2, pady=10)

    back_btn = tk.Button(frame, text="Back", command=lambda: [frame.destroy(), on_back()])
    back_btn.grid(row=7, column=0, columnspan=2)
