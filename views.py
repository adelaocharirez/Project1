import tkinter as tk
from tkinter import messagebox
from controllers import ElectionController
from storage import save_data  # import the save_data function

class MainApplication(tk.Tk):# creats tkinter window
    def __init__(self, controller: ElectionController):
        super().__init__()
        self.controller = controller

        self.title('Voting System')
        self.geometry('300x200')

        tk.Label(self, text="Vote for a Candidate").pack()

        for candidate_name in controller.get_candidate_names():
            button = tk.Button(self, text=candidate_name,
                               command=lambda c=candidate_name: self.vote(c))
            button.pack()

        results_button = tk.Button(self, text="Show Results", command=self.show_results)
        results_button.pack()

        # Add a Reset Button
        reset_button = tk.Button(self, text="Reset Votes", command=self.reset_votes)
        reset_button.pack()

    def vote(self, candidate_name: str): # Vote handling + Confirmation
        self.controller.vote_for_candidate(candidate_name)
        messagebox.showinfo("Vote", f"Voted for {candidate_name}")

    def show_results(self): #displays voting results
        results = self.controller.get_results()
        messagebox.showinfo("Results", results)

    def reset_votes(self):
        """Resets the votes and updates the UI accordingly."""
        self.controller.reset_votes()
        save_data(self.controller)  # Save the reset state to the file
        messagebox.showinfo("Reset", "The votes have been reset.")
        # Update any UI elements here if necessary
