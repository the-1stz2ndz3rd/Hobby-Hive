# utils/validation.py

def is_valid_signup(user_data):
    """
    Validates the sign-up form input.
    Expected keys in user_data:
    - name: str (at least 3 characters)
    - student_id: numeric string
    - username: str (at least 3 characters)
    - password: str (at least 6 characters)
    - bio: str (optional)
    - hobbies: list (must include at least one)
    """
    name = user_data.get("name", "").strip()
    student_id = user_data.get("student_id", "").strip()
    username = user_data.get("username", "").strip()
    password = user_data.get("password", "")
    hobbies = user_data.get("hobbies", [])

    if len(name) < 3:
        return False, "Full name must be at least 3 characters."
    if not student_id.isdigit():
        return False, "Student ID must be numeric."
    if len(username) < 3:
        return False, "Username must be at least 3 characters."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    if not isinstance(hobbies, list) or len(hobbies) == 0:
        return False, "Please select at least one hobby."

    return True, "Signup data is valid."

def is_valid_login(username, password):
    """
    Validates login credentials.
    """
    if not username.strip():
        return False, "Username cannot be empty."
    if not password:
        return False, "Password cannot be empty."
    return True, "Login data is valid."
