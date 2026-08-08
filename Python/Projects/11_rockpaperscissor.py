# Project 11: Rock Paper Scissor - Create a game that has users fight the machine
# Use 17 Notes
# Use the random library to have users fight a computer w/rock paper and scissors

# The random module will pick a random chocie for users to beat
import random

# Initialized tuple for options in rock, paper, scissors
options = ("rock", "paper", "scissors")

# Set is_running to bool to check state of game
is_running = True

print("Python RPS Game")
print("----------------")
print(f"Select between rock, paper, and scissors: ")
while (is_running):

    # Initialize player to store choice (None works like boolean)
    player = None
    # Initialized computer w/.choice(seq) method to print a random element from the tuple
    computer = random.choice(options)

    try:    # Get user input for choice
        player = input("Enter your guess: ").lower()

        # Check if user input is NOT IN options tuple
        while (player not in options):
            print("\nERROR: Invalid Input - Select Rock, Paper, or Scissors")
            player = input("Enter your guess: ").lower()

    except: # Will only print if error w/string occurs
        print("ERROR: Invalid Input - Select: Rock, Paper, or Scissors")
        continue

    # Print output to console
    if (player == computer):
        print("\nIt's a tie!")
    elif (player == "rock" and computer == "scissors"):
        print("\nYou Win!")
    elif (player == "paper" and computer == "rock"):
        print("\nYou Win!")
    elif (player == "scissors" and computer == "paper"):
        print("\nYou Win!")
    else:
        print("\nYou lose...")
            
    # Print the output
    print("----------------")
    print(f"  Player: {player}")
    print(f"Computer: {computer}\n")

    # Check to see if user wants to play again
    if not input("Play again? (Y/N): ").lower() == "y":
        is_running = False

print("\nThanks for playing!")