# Project 13: Banking Program - Create a banking program with functions and utilizing the main method
# Uses Notes 18-28
# Use the main module to create a menu-driven banking program.

# Show user thier account balance
def show_balance(balance):
    print("\n--- Account Balance ---")
    print(f"Your account balance is ${balance:>15,.2f}\n")

# Show user their deposit amount
def deposit():
    amount = 0.0
    is_valid = True

    print("\n---- Deposit Funds ----")
    while is_valid:
        # Typecasting as a floating-point number and using exeception handling
        try: 
            amount = float(input("Enter an amount to be deposited: $"))

            # Handle formatting errors
            # Check if deposited amount is less than $0 (negative)
            if (amount < 0):
                print("ERROR: Out of Range - Deposit must be at least $0.01\n")
                continue
            # Check if deposited amount is greater than $25,000 (deposit cap)
            elif (amount > 25000):
                print("ERROR: Out of Range - Deposit is limited to $25,000\n")
                continue

        # Handle exception errors
        except:
            print("ERROR: Invalid Input - Digits only (0-9)\n")
            continue

        return amount

# Show user their withdraw amount
def withdraw():
    amount = 0.0
    is_valid = True

    print("\n--- Withdrawl Funds ---")
    while is_valid:
        # Typecasting as a floating-point number and using exeception handling
        try: 
            amount = float(input("Enter an amount to be withdrawn: "))

            # Handle formatting errors
            # Check if withdrawn amount is less than $0 (negative)
            if (amount < 0):
                print("ERROR: Out of Range - Withdrawl must be at least $0.01\n")
                continue
            # Check if withdrawn amount is greater than $50,000 (withdrawl cap)
            elif (amount > 50000):
                print("ERROR: Out of Range - Withdrawl is limited to $50,000\n")
                continue

        # Handle exception errors
        except:
            print("ERROR: Invalid Input - Digits only (0-9)\n")
            continue

        return amount

# Show user the main menu options
def menu():
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("-----------------------")

# Program execution starts here
def main():
    balance = 0.0
    amount = 0.0
    is_running = True

    print("--- Banking Program ---")
    # Call the menu() function
    menu()
    # If is_running = False, exit the while loop
    while is_running:
        # Typecasting as an integer and using exeception handling
        try: 
            choice = int(input("Enter Menu Option (1-4): "))

            if (choice < 1 or choice > 4):
                print("ERROR: Out of Range - Value in between (1-4)\n")
                continue
        except:
            print("ERROR: Invalid Input - Digits only (0-4)\n")
            continue

        match (choice):
            case 1:
                # Call the show_balance() function
                show_balance(balance)
            case 2:
                # Call the deposit() function and add the current balance for new amount
                amount = deposit()
                balance += amount
                print(f"You have deposited  ${amount:>15,.2f}")
                print(f"Your new balance is ${balance:>15,.2f}\n")
            case 3:
                # Call the withdraw() function and subtract the current balance for new amount
                amount = withdraw()
                balance -= amount
                print(f"You have withdrawn  ${amount:>15,.2f}")
                print(f"Your new balance is ${balance:>15,.2f}\n")
            case 4:
                # Exit the loop
                is_running = False

    print("Exiting the program...")

# The program starts by checking if filename is main
if __name__ == "__main__":
    # `__` is refered to as "dunder"
    # print(f"Called main.py file is: {__name__}\n")
    main()
    # print("Exiting main.py file...")