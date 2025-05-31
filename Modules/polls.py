# modules/polls.py
from utils.data_storage import load_json, save_json

POLLS_FILE = "data/polls.json"

def get_polls():
    return load_json(POLLS_FILE)

def add_poll(poll):
    polls = load_json(POLLS_FILE)
    if not isinstance(polls, list):
        polls = []
    polls.append(poll)
    save_json(POLLS_FILE, polls)

def vote_poll(poll_id, option):
    polls = load_json(POLLS_FILE)
    for poll in polls:
        if poll.get("id") == poll_id:
            poll["votes"][option] = poll["votes"].get(option, 0) + 1
            break
    save_json(POLLS_FILE, polls)
