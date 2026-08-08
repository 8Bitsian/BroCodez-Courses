# Project 10: Number Guessing Game - Create a game that has users guess what was generated
# Use 17 Notes
# Use the random library to have users guess what was generated

# Thanks to you to @ikiwq_ on Twitch
# Thanks to you to @EynonPlays on Twitch

# The random module will pick a random number for user to guess 
import random

# Initialize variables for lowest and highest numbers in range
low_num = 1
high_num = 100

# Initialize answer to random number generated using .randint() method
answer = random.randint(low_num, high_num)

# Initialize guess to store number of tries the end user guesses the number
guesses = 0

# Set is_running to bool to check state of game
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low_num} and {high_num}")
while (is_running):
    # Thanks you to @ikiwq_ on Twitch
    try:
        # Prompt the user for initial guess
        # Typecasting as an integer and using exception handling
        guess = int(input("Enter your guess: "))

        # Check if guess is out of range
        if (guess < low_num or guess > high_num):
            print("ERROR: Out of Range - Value in (1-100)")
            print(f"Select a number between {low_num} and {high_num}: ")
            continue
    except:
        print("ERROR: Invalid Input - Digits only (0-9)")
        print(f"Select a number between {low_num} and {high_num}: ")
        # Thanks you to @EynonPlays on Twitch
        continue

    # Increase the guess count by 1
    guesses += 1

    if (guess < answer):
        print("Too low! Try again!")
    elif (guess > answer):
        print("Too high! Try again!")
    else:
        print(f"CORRECT: The answer is {answer}")
        print(f"Number of Guesses: {guesses}")
        break    