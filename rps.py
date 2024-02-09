import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        # Create variables to keep track of player and computer choices
        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()

        # Label to display computer choice
        self.computer_label = tk.Label(root, text="Computer's Choice:", font=("Helvetica", 12))
        self.computer_label.grid(row=0, column=0, padx=10, pady=10)

        # Label to display player choice
        self.player_label = tk.Label(root, text="Your Choice:", font=("Helvetica", 12))
        self.player_label.grid(row=1, column=0, padx=10, pady=10)

        # Label to display game result
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for player choices
        choices = ["Rock", "Paper", "Scissors"]
        for idx, choice in enumerate(choices):
            button = tk.Button(root, text=choice, width=10, font=("Helvetica", 12),
                                command=lambda c=choice: self.play(c))
            button.grid(row=1, column=idx+1, padx=5, pady=5)

    def play(self, player_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        self.player_choice.set(player_choice)
        self.computer_choice.set(computer_choice)

        if player_choice == computer_choice:
            self.result_label.config(text="It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            self.result_label.config(text="You win!")
        else:
            self.result_label.config(text="Computer wins!")

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
