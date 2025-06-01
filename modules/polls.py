# modules/polls.py

import uuid
from utils.data_storage import load_json, save_json

POLLS_FILE = "data/polls.json"

def get_polls():
    """
    Returns a list of all polls.
    Each poll has: id, question, options (list), votes (dict), created_by, group
    """
    polls = load_json(POLLS_FILE)
    return polls if isinstance(polls, list) else []

def add_poll(question, options, created_by, group=None):
    """
    Creates a new poll.
    Params:
        - question (str): Poll question
        - options (list of str): List of answer options
        - created_by (str): Username
        - group (str): Optional, hobby group
    Returns: (bool, str)
    """
    if not question or not options or not isinstance(options, list):
        return False, "Invalid poll data."

    poll = {
        "id": str(uuid.uuid4()),
        "question": question,
        "options": options,
        "votes": {option: 0 for option in options},
        "created_by": created_by,
        "group": group
    }

    polls = get_polls()
    polls.append(poll)
    save_json(POLLS_FILE, polls)
    return True, "Poll created successfully."

def vote_poll(poll_id, option):
    """
    Adds a vote to a specific option in a poll.
    """
    polls = get_polls()
    for poll in polls:
        if poll.get("id") == poll_id:
            if option in poll["votes"]:
                poll["votes"][option] += 1
                save_json(POLLS_FILE, polls)
                return True, "Vote counted!"
            else:
                return False, "Invalid option."
    return False, "Poll not found."

def get_poll_by_id(poll_id):
    """
    Retrieve a specific poll by its unique ID.
    """
    polls = get_polls()
    return next((poll for poll in polls if poll.get("id") == poll_id), None)
