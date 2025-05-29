import os
import random

ICEBREAKERS = [
    "If you could instantly learn any skill, what would it be?",
    "If you could travel anywhere right now, where would you go?",
    "What’s your favorite way to relax after a busy day?",
    "What’s a hobby you’ve always wanted to try but haven’t yet?",
    "If you had a superpower, what would it be?"
]

def get_chat_filename(user1, user2):
    return f"chat_{'_'.join(sorted([user1, user2]))}.txt"

def load_private_chat(user1, user2):
    filename = get_chat_filename(user1, user2)
    if not os.path.exists(filename):
        return[]
    with open(filename, "r") as file:
        return file.readlines()

def save_private_message(user1, user2, message):
    filename = get_chat_filename(user1, user2)
    with open(filename, "a") as file:
        file.write(f"{user1}: {message}\n")

def display_private_chat_ui(user1, user2):
    chat = load_private_chat(user1, user2)
    print(f"\n--- chat between {user1} and {user2} ---")
    for line in chat:
        print(line.strip())
    print(f"Icebreaker: {random.choice(ICEBREAKERS)}")
    while True:
        msg = input(f"{user1} > ")
        if msg.lower() == "exit":
            break
        save_private_message(user1, user2, msg)
        print("message sent")
