import json
from models import Candidate  # imports class

def save_data(controller):
    """Saves the current vote count to a file."""
    with open('vote_data.json', 'w') as file:
        data = {candidate.name: candidate.votes for candidate in controller.candidates}
        json.dump(data, file)

def load_data(controller):
    """Loads the vote count from a file."""
    try:
        with open('vote_data.json', 'r') as file:
            data = json.load(file)
            controller.candidates.clear()  # clear any existing candidates before loading
            for name, votes in data.items():
                candidate = Candidate(name)  # create a new Candidate instance
                candidate.votes = votes
                controller.candidates.append(candidate)
    except FileNotFoundError:
        pass
