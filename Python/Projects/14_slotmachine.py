# Project 14: Slot Machine Program - Uses Notes 18-28
# Create a slot machine program using functions and the main method.

# Easter egg delivered by @omp3policeo on Twitch
# from __future__ import braces
import random
import time

# Allow user to place bet
def place_bet(balance):
    amount = 0.0
    is_valid = True

    print("\n---- Place Your Bet ----")
    while is_valid:
        # Typecasting as a floating-point number and using exeception handling
        try: 
            amount = float(input("Gambled Amount: $"))

            # Handle formatting errors
            # Check if amount is greater than current balance (check for funds)
            if (amount > balance):
                print("WARNING: Insufficient Funds - You are gambling without funds\n")
                return amount
                break
            # Check if gambled amount is less than $0 (negative)
            elif (amount < 0):
                print("ERROR: Out of Range - Deposit must be at least $1\n")
                continue
            # Check if gambled amount is greater than $25,000 (deposit cap)
            elif (amount > 5000):
                print("ERROR: Out of Range - Deposit is limited to $5000\n")
                continue
        # Handle exception errors
        except:
            print("ERROR: Invalid Input - Digits only (0-9)\n")
            continue
        
        return amount

# Generate new string for row when spun
def spin_row():
    # Create a symbols list w/strings
    symbols = ["🍋", "🍒", "🍌", "🍇", "⭐"]

    # Use list comprehensions: [(expression) `for` value `in` iterable `if` (condition)]
    # The underscore (_) is a wild card so it essentially means every iteration
    return [(random.choice(symbols)) for _ in range(3) ]

# suggested by @EynonPlays on Twitch
def animate_spin():
    # Create a symbols list w/strings
    symbols = ["🍋", "🍒", "🍌", "🍇", "⭐"]

    for symbol in range(3):
        print(f"{random.choice(symbols)} | {random.choice(symbols)} | {random.choice(symbols)}", end="\r")
        time.sleep(0.5)
    
# Print new string to console
def print_row(row):
    print("\n~~~~~~~~~~~~")
    # Call the animate_spin() function to take the place of "spinning..."
    animate_spin()
    # the .join() method combines indices with strings
    print(" | ".join(row))
    print("~~~~~~~~~~~~\n")

# Give user payout if symbols are matching
def get_payout(row, bet):
    # Check if all three symbols in row are the same
    if row[0] == row[1] == row[2]:
        # Check one index (pos 0) is the same as symbol
        if row[0] == "🍋":
            return bet
        elif row[0] == "🍒":
            return bet * 2
        elif row[0] == "🫐":
            return bet * 3
        elif row[0] == "🍇":
            return bet * 4
        elif row[0] == "⭐":
            return bet * 5
    return 0

# Print messages depending on win/lose conditions
# Credit to @omp3police0 and @EynonPlays
def win_lose(balance):
    if (balance >= 500000):
        print("You took the House... 🏡\n")
    elif (balance >= 5000):
        print("Congrats! You win!\n")
    elif (balance <= -500000):
        print("The House wins your house... 🏚️\n")
    elif (balance <= -5000):
        print("The House always wins...\n")
    else:
        print("One more roll... 🎰\n")

def play_game(balance):
    # Call the place_bet() function and pass in the balance
    bet_amount = place_bet(balance)
    balance -= bet_amount

    # Call the spin_row() function
    row = spin_row()

    # Call the print_row() function
    print_row(row)

    # Call the get_payout() function and pass in row/bet_amount
    payout = get_payout(row, bet_amount)

    if payout > 0:
        print(f"You won ${payout:.2f}\n")
        balance += payout
    else:
        print(f"The house won this round...\n")

    # Call win_condition() function
    win_lose(balance)

# Print main menu options to console
def menu(balance):
    print("~~~~~~~ WELCOME TO PYSLOTS ~~~~~~~")
    print(" Symbols: 🍋 | 🍒 | 🍌 | 🍇 | ⭐")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Current Balance: ${balance:>16,.2f}")
    print("\n~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~")
    print("1. Place Bet")
    print("2. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Program execution starts here
def main():
    balance = 100.0
    amount = 0.0
    is_running = True
    play_again = True

    # If is_running = False, exit the while loop
    while is_running:
        # Call the menu() function
        menu(balance)

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
                # Determine if user want to play again
                while play_again:
                    # Call the replay() function and pass in the balance
                    play_game(balance)

                    try:
                        try_again = input("Spin? (Y/N) ").lower()

                        if (try_again != "y"):
                            print("\nAlways welcome to try again!\n")
                            play_again = False
                            break
                    except:
                        print("ERROR: Invalid Input - Characters only (Y or N)\n")
                        continue
            case 2:
                # Exit the loop
                is_running = False

    # print("Exiting the program...")

# The program starts by checking if filename is main
if __name__ == "__main__":
    # `__` is refered to as "dunder"
    # print(f"Called main.py file is: {__name__}\n")
    main()
    # print("Exiting main.py file...")