import json
from datetime import datetime

def save_feedback(prompt, response):
    entry = {
        "time": str(datetime.now()),
        "prompt": prompt,
        "response": response
    }

    with open("data/learning.json", "a") as f:
        f.write(json.dumps(entry) + "\n")