# profile.py

def display_profile(user):
    print("=== Your Profile Summary ===")
    print(f"Name       : {user['full_name']}")
    print(f"Student ID : {user['student_id']}")
    print(f"Username   : {user['username']}")
    print(f"Hobbies    : {', '.join(user['hobbies'])}")
    print(f"Bio/Status : {user['bio']}")
    print("\n🎯 You've been added to the following hobby groups:")
    for hobby in user["hobbies"]:
        print(f"   • {hobby} Group")
