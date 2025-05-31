# utils/validation.py

def is_valid_signup(user_data):
    """
    Validate signup data dictionary.
    Expected keys: name, student_id, username, password, bio, hobbies(list)
    """
    if not user_data.get("name") or len(user_data["name"].strip()) < 3:
        return False, "Full name must be at least 3 characters."
    if not user_data.get("student_id") or not user_data["student_id"].isdigit():
        return False, "Student ID must be numeric."
    if not user_data.get("username") or len(user_data["username"].strip()) < 3:
        return False, "Username must be at least 3 characters."
    if not user_data.get("password") or len(user_data["password"]) < 6:
        return False, "Password must be at least 6 characters."
    if not isinstance(user_data.get("hobbies"), list) or len(user_data["hobbies"]) == 0:
        return False, "At least one hobby must be specified."
    # Add more validations as needed
    return True, "Valid signup data."

def is_valid_login(username, password):
    if not username or len(username.strip()) == 0:
        return False, "Username cannot be empty."
    if not password or len(password) == 0:
        return False, "Password cannot be empty."
    return True, "Valid login data."
