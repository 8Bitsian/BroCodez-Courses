# Project 16: Hangman Game - Uses Notes 18-28
# Create a hangman game using functions and the main method w/1D arrays and switch statements.

import random

# Calls values from wordlist.py and hangmanart.py
from wordslist import words
from hangmanart import hangman_art

# Generate new string (word) when called
# @Eynon reminded me that you can store collections in functions
def gen_word():
    # Chooses random values from words using random.choice() method
    return random.choice(words)

def display_man(wrong_guesses):
    print("\n~~~~~~~ HANGMAN ~~~~~~~")
    for line in hangman_art[wrong_guesses]:
        print(f"         {line}         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~")

def display_hint(hint):
    print(" ".join(hint))
    print("~~~~~~~~~~~~~~~~~~~~~~~")

def display_answer(answer):
    print(" ".join(answer))
    print("~~~~~~~~~~~~~~~~~~~~~~~")

def play_game(wrong_guesses):
    pass

def menu():
    print("\n~~~~~~ MAIN MENU ~~~~~~")
    print("1. Play")
    print("2. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~")

# Program execution begins here
def main():
    # Initialize boolean variable to run program
    is_running = True

    while (is_running):
        # Choose a word with the random.choice() method
        answer = gen_word()
        # Generater a list of underscore character by the len() method
        hint = ["_"] * len(answer)

        # Call main menu() function
        menu()

        # Typecasting as an integer and using exeception handling
        try: 
            choice = int(input("Enter Menu Option: "))

            if (choice < 1 or choice > 2):
                print("ERROR: Out of Range - Value in between (1-2)\n")
                continue
        except:
            print("ERROR: Invalid Input - Single digits only (1-2)\n")
            continue

        match (choice):
            case 1:
                # Resets every time we choose option 1
                play_again = True

                # Initialize integer number of wrong guesses
                wrong_guesses = 0
                # Initialize an empty set with the set() method to keep a set of guessed letters
                guessed_letters = set()

                # Determine if user want to play again
                while (play_again):
                    # Call the replay() function and pass in the balance
                    display_man(wrong_guesses)
                    display_hint(hint)

                    try:
                        guess = input("Enter a letter: ").lower()
                        # If the length of our guess is longer than 1 or if our guess is numerical
                        if (len(guess) != 1):
                            print("ERROR: Invalid Input - One character only (a-z or A-Z)\n")
                            continue
                        if (guess.isdigit()):
                            print("ERROR: Invalid Input - One character only (a-z or A-Z)\n")
                            continue
                        if (guess in guessed_letters):
                            print(f"{guess} has already been used.")
                            continue
                        guessed_letters.add(guess)
                    except:
                        print("ERROR: Invalid Input - One character only (a-z or A-Z)\n")
                        continue
                    
                    if (guess in answer):
                        for index in range(len(answer)):
                            if (answer[index] == guess):
                                hint[index] = guess
                    else:
                        wrong_guesses += 1

                    if "_" not in hint:
                        display_man(wrong_guesses)
                        display_answer(answer)
                        print("YOU WIN!")
                        play_again = False
                    elif wrong_guesses >= 6:
                        display_man(wrong_guesses)
                        display_answer(answer)
                        print("You Lose...")
                        play_again = False
            case 2:
                # Exit the loop
                is_running = False

# The program starts by checking if filename is main
if __name__ == "__main__":
    main()