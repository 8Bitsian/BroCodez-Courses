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
    print("\n~~~~~~~~~ PLACE YOUR BET ~~~~~~~~~")
    while is_valid:
        # Typecasting as a floating-point number and using exeception handling
        try:
            # Get user input for amount to bet on
            amount = float(input("Gambled Amount: $"))

            # Handle formatting errors (had less than come first)
            # Check if gambled amount is less than $1 ($0 or negative)
            if (amount < 1):
                print("ERROR: Out of Range - Deposit must be at least $1\n")
                continue
            # Check if gambled amount is greater than $25,000 (deposit cap)
            elif (amount > 5000):
                print("ERROR: Out of Range - Deposit is limited to $5000\n")
                continue
            # Check if amount is greater than current balance (check for funds)
            elif (amount > balance):
                print("WARNING: Insufficient Funds - You are gambling without funds\n")
                return amount
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
    return [(random.choice(symbols)) for _ in range(5) ]

# suggested by @EynonPlays on Twitch
def animate_spin():
    # Create a symbols list w/strings
    symbols = ["🍋", "🍒", "🍌", "🍇", "⭐"]

    # Repeat the spinning animation 4 times
    for symbol in range(4):
        # Replaced w/list comprehension to pick 5 random emojis from the symbols list
        emojis = [random.choice(symbols) for _ in range(5)]
        # The " | ".join(emojis) combines the 5 emojis in a single line
        # The end="\r" (carraige return) prints over the same console line
        # The flush=True forces the output to appear immediately
        print(f"  ~~~ " + " | ".join(emojis) + " ~~~ ", end="\r", flush=True)
        # Pauses each loop (frame) so animation is visible
        time.sleep(0.5)
    
# Print new string to console
def print_row(row):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Call the animate_spin() function to take the place of "spinning..."
    animate_spin()
    # the .join() method combines indices with strings
    print(f"  ~~~ " + " | ".join(row) + " ~~~ ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Give user payout if symbols are matching
def get_payout(row, bet):
    # Check if all five symbols in row are the same
    if row[0] == row[1] == row[2] == row[3] == row[4]:
        # Replace if-else statements w/dictionary
        symbol = row[0]
        multipliers = {"🍋": 1,
                       "🍒": 2,
                       "🍌": 3,
                       "🍇": 4,
                       "⭐": 5
        }
        # Check one index (pos 0) is the same as symbol
        return bet * multipliers[symbol]
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

def play_game(balance):
    # Get user input to place a betting amount
    bet_amount = place_bet(balance)
    balance -= bet_amount

    # Print the randomly generated slots
    row = spin_row()
    print_row(row)

    # Call the get_payout() function and pass in row/bet_amount
    payout = get_payout(row, bet_amount)

    if payout > 0:
        print(f"You won ${payout:,.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        balance += payout
    else:
        print(f"The house won this round...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        balance -= payout

    # Call win_condition() function
    win_lose(balance)

    return balance

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
                # Resets every time we choose option 1
                play_again = True

                # Determine if user want to play again
                while play_again:
                    # Call the replay() function and pass in the balance
                    balance = play_game(balance)

                    try:
                        try_again = input("One more roll... 🎰 Spin? (Y/N) ").lower()

                        if (try_again != "y"):
                            print("\nAlways welcome to try again!\n")
                            play_again = False
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