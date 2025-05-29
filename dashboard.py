def display_dashboard(user):
  print("welcome," " + user['name'] + "!")
        print("look who shares your hobby")

        for match in user.get("matches", []):
            print("- " + match['name'] + " | hobby: " + match['hobby'])

def search_users()
    users = [
        {"name":"Abebe","hobby": painting"}
        {"name":"Rahel","hobby":gaming"}
        {"name":"Bisrat","hobby":"photography"}]       
querr = input("Enter a name or hobby to search: ")
print("search result for '" + "':")
found = false
for user in users:
    if query.lower() in user['name'].lower() or query.lower() in user['hobby'].lower()
       print("- " + user['name']) + "| Hobby: " + user['hobby'])
       found = True 
    if not found:
       print("No users found.")
dark_mode_enabled = false

def toggle_dark_mode_enabled
    global dark_mode_enabled
    dark_mode_enabled = not dark_mode_enabled
    if dark_mode_enabled:
       print("Dark mode enabled.")
    else:
       print("Light mode enabled.")
def get_user_info() 
    name = input("Enter your name: ")
    matches = [
              {"name": "Abebe", " hobby": "painting"}
              {"name":"Rahel", "hobby": "gaming"},
      ]
      return {"name": name, "matches": matches}
Finished writing dashboad.py      
