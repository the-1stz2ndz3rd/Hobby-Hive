from users_data import users

def search_users(query):
    results = []
    for username, data in users.items():
        if query.lower() in data["name"].lower() or query.lower() in [h.lower() for h in data["hobbies"]]:
            results.append(username)
    return results
        
            
