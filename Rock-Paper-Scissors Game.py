import random

def print_instructions():
    print("Welcome to Rock, Paper, Scissors!")
    print("----------------------------------")
    print("Instructions:")
    print("• Type 'rock', 'paper', or 'scissors' to make your move.")
    print("• The computer will randomly pick one too.")
    print("• Rock beats scissors, scissors beat paper, paper beats rock.")
    print("• After each round, you'll see both choices and the result.")
    print("• Scores are tracked. Play as many rounds as you wish.\n")

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    print(result)

def play_again_prompt():
    while True:
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again in ['y', 'n']:
            return play_again == 'y'
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def play_game():
    print_instructions()
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        display_result(user_choice, computer_choice, result)
        print(f"Current Scores: You = {user_score} | Computer = {computer_score}")

        if not play_again_prompt():
            print(f"\nFinal Scores: You = {user_score} | Computer = {computer_score}")
            print("Thank you for playing! Goodbye!")
            break

        round_num += 1

# To run the game, uncomment the next line
play_game()
