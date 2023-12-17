import random

def get_user_choice():
    """Get user choice for Stone, Paper, Scissors."""
    print("Enter your choice: Stone, Paper, or Scissors")
    user_choice = input().strip().lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['stone', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'stone' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'stone') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """Main function to run the Stone, Paper, Scissors game."""
    print("Welcome to the Stone, Paper, Scissors game!")

    while True:
        user_choice = get_user_choice()
        if user_choice not in ['stone', 'paper', 'scissors']:
            print("Invalid choice. Please enter Stone, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Do you want to play again? (yes/no)")
        play_again = input().strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()

