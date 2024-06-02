import random

class ConsoleRockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

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
        print(f"Your score: {self.user_score}, Computer score: {self.computer_score}")

    def run(self):
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
            if user_choice not in self.choices:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                continue
            computer_choice = self.generate_computer_choice()
            print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            self.display_scores()
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = ConsoleRockPaperScissors()
    game.run()
