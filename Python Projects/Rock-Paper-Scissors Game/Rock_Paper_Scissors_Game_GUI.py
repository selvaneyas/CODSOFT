import tkinter as tk
from PIL import Image, ImageTk
import random

class GuiRockPaperScissors(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rock-Paper-Scissors Game")
        self.geometry("400x600")
        self.resizable(0, 0)

        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self, text="Rock-Paper-Scissors Game", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # User choice section
        self.user_choice_label = tk.Label(self, text="Your choice:", font=("Arial", 12))
        self.user_choice_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)

        self.rock_image = self.load_image("images/rock.png")
        self.paper_image = self.load_image("images/paper.png")
        self.scissors_image = self.load_image("images/scissors.png")

        self.rock_button = tk.Button(self.buttons_frame, image=self.rock_image, command=lambda: self.play_game('rock'))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, image=self.paper_image, command=lambda: self.play_game('paper'))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, image=self.scissors_image, command=lambda: self.play_game('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Computer choice section
        self.computer_choice_label = tk.Label(self, text="Computer's choice:", font=("Arial", 12))
        self.computer_choice_label.pack(pady=10)

        self.computer_choice_image_label = tk.Label(self)
        self.computer_choice_image_label.pack()

        self.computer_choice_var = tk.StringVar()
        self.computer_choice_text_label = tk.Label(self, textvariable=self.computer_choice_var, font=("Arial", 12))
        self.computer_choice_text_label.pack()

        # Result section
        self.result_label = tk.Label(self, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=20)

        # Score section
        self.score_label = tk.Label(self, text="Your score: 0, Computer score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Play again and Quit buttons
        self.play_again_button = tk.Button(self, text="Play Again", font=("Arial", 12), command=self.reset_game)
        self.play_again_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.quit_button = tk.Button(self, text="Quit", font=("Arial", 12), command=self.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=20, pady=20)

        # Information about the game
        self.info_label = tk.Label(self, text="Rock beats Scissors, Scissors beats Paper, Paper beats Rock.", font=("Arial", 10), wraplength=350, justify="center")
        self.info_label.pack(pady=10)

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((100, 100), Image.LANCZOS)  # Resize image to 100x100 pixels
        return ImageTk.PhotoImage(image)

    def generate_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def display_scores(self):
        self.score_label.config(text=f"Your score: {self.user_score}, Computer score: {self.computer_score}")

    def reset_game(self):
        self.computer_choice_image_label.config(image='')
        self.computer_choice_var.set('')
        self.result_label.config(text="")
        self.display_scores()

    def play_game(self, user_choice):
        computer_choice = self.generate_computer_choice()
        self.computer_choice_var.set(computer_choice)

        if computer_choice == 'rock':
            self.computer_choice_image_label.config(image=self.rock_image)
        elif computer_choice == 'paper':
            self.computer_choice_image_label.config(image=self.paper_image)
        elif computer_choice == 'scissors':
            self.computer_choice_image_label.config(image=self.scissors_image)

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)
        self.display_scores()

if __name__ == "__main__":
    app = GuiRockPaperScissors()
    
    # Window Icon
    window_icon = ImageTk.PhotoImage(file="images/game.png")
    app.iconphoto(False, window_icon)
    
    app.mainloop()
