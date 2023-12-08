from models import Candidate

class ElectionController:
    """Controller to manage election operations."""
    def __init__(self): # empty list
        self.candidates = []

    def add_candidate(self, name: str):
        """Adds a new candidate to the election."""
        self.candidates.append(Candidate(name))

    def vote_for_candidate(self, candidate_name: str):
        """Records a vote for a specified candidate."""
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.add_vote()
                return True
        return False

    def get_results(self) -> str:
        """Returns a string with the voting results."""
        return "\n".join(f"{c.name}: {c.votes} votes" for c in self.candidates)

    def get_candidate_names(self) -> list:
        """Returns a list of candidate names."""
        return [c.name for c in self.candidates]
       
    def reset_votes(self):
        """Resets the votes for all candidates."""
        for candidate in self.candidates:
            candidate.votes = 0
