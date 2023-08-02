from pathlib import Path
from typing import Dict
import json


ENV_DICT: Dict[str, str] = {}


with Path(".env").open("r") as env:
    for line in env:
        line = line.strip()
        if "=" not in line:
            continue

        frags = line.split("=")
        ENV_DICT[frags[0].lower()] = frags[1] 


MESSAGES = []
with Path("messages.json").open("r") as message_file:
    MESSAGES = json.load(message_file)
