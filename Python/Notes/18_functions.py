# Functions

# Instead of re-writing code, we can utilize functions to reference entire code blocks as reusable code
# To initialize a function, use the keyword def (for defintion/define) and the function name
def bdaySong():
    # Indent the codeblock after the function definition
    print("Happy Birthday to you!")
    print("You're a year older whoo-hoo!")
    print("Happy birthday dear friend~")
    print("Happy birthday to you!")
    print()

# # To call (invoke) the function type the function name w/parentheses [if_name()]
bdaySong()

# # You can send data into a function as arguments
# # When sending data, be sure to have matching set of parameters
def birthday(name, age):
    print(f"Happy birthday {name}!")
    print(f"You are {age} years old today!")
    print()

name = input("What is your name? ")
age = input("What is your age? ")

birthday(name, age)

# The return statement is used at the end of a function and sends a result back to the caller
# Ex. "z = funct(x, y)" is like using the assignment operator for z = result of function

# Created a function to return two arguments after addition
def add(x, y):
    z = x + y
    return z

# Created a function to return two arguments after subtraction
def subtract(x, y):
    # Thank you @EynonPlays on Twitch
    # Instead of using another variable, directly return result of operation
    return (x - y)

# Created a function to return two arguments after multiplication
def multiply(x, y):
    return (x * y)

# Created a function to return two arguments after division
def divide(x, y):
    return (x / y)

x = float(input("Enter x: "))
y = float(input("Enter y: "))
print()

print(add(x, y))
print(subtract(x, y))
print(mutiply(x, y))
print(divide(x, y))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bit", "software")

print(full_name)