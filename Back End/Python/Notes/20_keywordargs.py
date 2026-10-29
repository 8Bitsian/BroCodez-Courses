# Keyword Arguments

# # A keyword argument is an arg. preceded by an identifier to help w/readability.
def hello(greeting, f_name, l_name, title="Mx."):
    print(f"{greeting}, {title}{f_name} {l_name}\n")

arg1 = input("Enter Greeting: ")
arg3 = input("Enter First Name: ")
arg4 = input("Enter Last Name: ")

# # Order of keyword arguments doesn't matter; Be sure to put position arg. first
# # Else you get "SyntaxError: Postional argument follows keyword argument"
hello(arg1, f_name=arg3, l_name=arg4) # Prints "Hello, Ms.8Bit Software"

# # This is used for clarification so args. always appear in the order you set them
hello(arg1, l_name=arg3, f_name=arg4) # Prints "Hello, Software 8Bit"

for x in range (1, 4):
    # print(x)    # Print "1 2 3" on newlines
    # End is a keyword argument for the bulit-in print statement
    print(x, end=" ")   # Print "1 2 3" on same line
print()

# Sep is a keyword arg. for the print() which outputs character(s) between strings
print("1", "2", "3", sep="-")