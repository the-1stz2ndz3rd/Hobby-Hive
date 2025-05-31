import tkinter as tk
from modules import user_auth, user_profiles, group_chat, settings
from utils.ui_helpers import apply_theme
from config import APP_TITLE

# Initialize the main app window
class HobbyHiveApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        apply_theme(self.root)  # Light/dark mode theme

        self.display_welcome_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def display_welcome_screen(self):
        self.clear_screen()

        logo_label = tk.Label(self.root, text="🐝 Hobby Hive", font=("Helvetica", 28, "bold"))
        logo_label.pack(pady=40)

        login_btn = tk.Button(self.root, text="Log In", width=20, command=self.display_login)
        signup_btn = tk.Button(self.root, text="Sign Up", width=20, command=self.display_signup)

        login_btn.pack(pady=10)
        signup_btn.pack(pady=10)

    def display_login(self):
        self.clear_screen()
        user_auth.login_screen(self.root, self.navigate_to_dashboard, self.display_welcome_screen)

    def display_signup(self):
        self.clear_screen()
        user_auth.signup_screen(self.root, self.navigate_to_dashboard, self.display_welcome_screen)

    def navigate_to_dashboard(self, username):
        self.clear_screen()
        user_profiles.dashboard_screen(self.root, username)

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HobbyHiveApp(root)
    root.mainloop()
