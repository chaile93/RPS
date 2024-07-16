import random

def rock_paper_scissors():
    actions = ["Rock", "Paper", "Scissors"]

    while True:
        # Computer randomly chooses an action
        computer_action = random.choice(actions)

        # Player selects an action
        player_action = input("Enter your move (Rock/Paper/Scissors) or 'I quit' to end: ").strip().capitalize()

        if player_action == 'I quit':
            print("Thank you for playing!")
            break

        if player_action not in actions:
            print("Invalid input. Please enter Rock, Paper, Scissors, or 'I quit'.")
            continue

        print(f"Player chose: {player_action}")
        print(f"Computer chose: {computer_action}")

        # Determine the winner
        if player_action == computer_action:
            print("Game Tied!")
        elif (player_action == "Rock" and computer_action == "Paper") or \
             (player_action == "Paper" and computer_action == "Scissors") or \
             (player_action == "Scissors" and computer_action == "Rock"):
            print("You lose!")
        else:
            print("You win!")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
