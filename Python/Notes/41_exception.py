# Exception Handling
# An exception is an event that interupts the flow of a program (suchs as ZeroDivisionError, TypeError, ValueError, etc.)
# There are four parts to the exception handle:
# 1. `try` block lets you test code for errors
# 2. `except` block lets you handle the error
# 3. `else` block lets you execute code if there's no error
# 4. `finally` block lets you execute code regardless of the `try` and `except` blocks

# User input is cosidered dangerous and should be validated by the error handle blocks
def get_number():
    try:
        # Get user input
        number = int(input("Enter a number: "))
        print (1 / number)
    except ValueError:
        # If user tries to type alpha chars, print the following:
        print("ERROR: Value Error - Input must be a digit (0-9)")
        get_number()
    except ZeroDivisionError:
        # If user tries to divide by zero, print the following:
        print("ERROR: Zero Division - Cannot divide by zero.")
        get_number()
    # You can implement the `Exeception` keyword as a catch-all, but it is considered bad practice since it is too broad of a clause. Ex. except Exception:
    # Finally code blocks are usually used when opening and closing files.
    # finally:
    #     print("Do clean up...")

def try_again():
    try:
        again = input("Try again? (X to Exit, Y to Stay): ").lower()
        if again == "x":
            return again
        elif again == "y":
            pass
    except ValueError:
        # If user tries to type digits chars, print the following:
        print("ERROR: Value Error - Input must be a letter (A-Z)")
        try_again()
        
def main():
    while (True):
        # Call get_input
        number = get_number()
        
        # Call try_again
        again = try_again()
        if (again == 'x'):
            break

if __name__ == "__main__":
    main()