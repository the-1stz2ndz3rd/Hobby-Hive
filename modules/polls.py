import json
import os
from config import POLLS_FILE  # Define POLLS_FILE = "data/polls.json"
from modules.notifications import add_notification
from modules.user_auth import load_users

os.makedirs(os.path.dirname(POLLS_FILE), exist_ok=True)

def create_poll(user):
    question = input("Enter poll question: ")
    options = []
    print("Enter poll options (type 'done' to finish):")
    while True:
        option = input(f"Option {len(options)+1}: ").strip()
        if option.lower() == 'done':
            break
        if option:
            options.append(option)

    if len(options) < 2:
        print("❌ A poll needs at least 2 options.")
        return

    poll = {
        "question": question,
        "options": options,
        "votes": [0] * len(options),
        "creator": user["username"]
    }

    try:
        with open(POLLS_FILE, "r") as f:
            polls = json.load(f)
    except:
        polls = []

    polls.append(poll)

    with open(POLLS_FILE, "w") as f:
        json.dump(polls, f, indent=2)

    print("📊 Poll created successfully!")

# Notify the creator
    add_notification(user["username"], f"Poll '{question}' created successfully!")

# Notify all other users
    all_users = load_users()
    for u in all_users:
        if u["username"] != user["username"]:
            add_notification(u["username"], f"📢 New poll available: '{question}'")

def vote_in_poll(user):
    try:
        with open(POLLS_FILE, "r") as f:
            polls = json.load(f)
    except:
        print("📭 No polls available.")
        return

    if not polls:
        print("📭 No polls found.")
        return

    print("\n📊 Available Polls:")
    for i, poll in enumerate(polls):
        print(f"{i+1}. {poll['question']} (by {poll['creator']})")

    try:
        choice = int(input("Select poll number to vote in: ")) - 1
        poll = polls[choice]
    except (ValueError, IndexError):
        print("❌ Invalid choice.")
        return

    print(f"\n📋 {poll['question']}")
    for idx, option in enumerate(poll["options"], 1):
        print(f"{idx}. {option}")
    
    try:
        vote = int(input("Choose option number: ")) - 1
        if vote < 0 or vote >= len(poll["options"]):
            raise ValueError
        poll["votes"][vote] += 1
    except (ValueError, IndexError):
        print("❌ Invalid vote.")
        return

    with open(POLLS_FILE, "w") as f:
        json.dump(polls, f, indent=2)

    print("✅ Vote recorded.")
def view_poll_results():
    try:
        with open(POLLS_FILE, "r") as f:
            polls = json.load(f)
    except:
        print("📭 No poll data found.")
        return

    if not polls:
        print("📭 No polls to show.")
        return

    print("\n📈 Poll Results:")
    for poll in polls:
        print(f"\n🔸 {poll['question']}")
        total = sum(poll["votes"])
        for i, option in enumerate(poll["options"]):
            vote_count = poll["votes"][i]
            percent = (vote_count / total * 100) if total else 0
            print(f"   - {option}: {vote_count} vote(s) ({percent:.1f}%)")
        print("-" * 40)


