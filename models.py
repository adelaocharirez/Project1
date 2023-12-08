class Candidate:
    """Candidate model representing a candidate in an election."""
    def __init__(self, name: str):
        self.name = name
        self.votes = 0

    def add_vote(self):
        """Adds a vote to the candidate."""
        self.votes += 1

