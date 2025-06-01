#Modules/uer_profiles.py

import tkinter as tk
from utils.data_storage import load_json
from PIL import ImageTk, Image
import os

USERS_FILE = "data/users_data.json"
GROUP_DATA_FILE = "data/group_data.json"
GROUP_IMAGES_DIR = "assets/group_images"

def dashboard_screen(root, username):
    user = load_json(USERS_FILE).get(username)
    if not user:
        tk.Label(root, text="User not found").pack()
        return

    group_data = load_json(GROUP_DATA_FILE)
    hobbies = user.get("hobbies", [])

    # === Profile Summary ===
    profile_frame = tk.Frame(root)
    profile_frame.pack(pady=20)

    tk.Label(profile_frame, text=f"Welcome, {user['name']}!", font=("Helvetica", 18, "bold")).pack()

    tk.Label(profile_frame, text=f"Bio: {user.get('bio', '')}", font=("Helvetica", 12)).pack(pady=5)

    hobbies_str = ", ".join(hobbies)
    tk.Label(profile_frame, text=f"Hobbies: {hobbies_str}", font=("Helvetica", 12)).pack()

    # === Hobby Groups ===
    groups_frame = tk.LabelFrame(root, text="Your Hobby Groups", padx=10, pady=10)
    groups_frame.pack(padx=10, pady=20)

    for hobby in hobbies:
        group_info = group_data.get(hobby.lower())
        image_path = os.path.join(GROUP_IMAGES_DIR, f"{hobby}.jpg")

        group_row = tk.Frame(groups_frame)
        group_row.pack(fill="x", pady=5)

        # Load group image
        try:
            img = Image.open(image_path)
            img = img.resize((50, 50))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(group_row, image=photo)
            img_label.image = photo
            img_label.pack(side="left", padx=10)
        except Exception:
            tk.Label(group_row, text="🖼️").pack(side="left", padx=10)

        # Group info
        group_text = f"{hobby}\n“{group_info['tagline']}”" if group_info else hobby
        tk.Label(group_row, text=group_text, font=("Helvetica", 12)).pack(side="left")

        # Join Chat button
        btn = tk.Button(group_row, text="Enter Chat", command=lambda h=hobby: print(f"Enter {h} chat"))
        btn.pack(side="right")

    # === Other Placeholder Sections ===
    tk.Label(root, text="🧩 People You Match With (coming soon...)").pack(pady=10)
    tk.Label(root, text="🔍 Search bar (coming soon...)").pack()
    tk.Label(root, text="🌙 Dark Mode toggle (coming soon...)").pack()
