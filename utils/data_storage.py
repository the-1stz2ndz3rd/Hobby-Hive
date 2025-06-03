import os
import json
from config import USER_DATA_FILE, GROUP_DATA_FILE, ICEBREAKERS_FILE

def init_data():
    for file in [USER_DATA_FILE, GROUP_DATA_FILE, ICEBREAKERS_FILE]:
        if not os.path.exists(file):
            with open(file, "w") as f:
                json.dump([], f)
