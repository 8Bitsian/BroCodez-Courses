# While Loops - A basic form of decision making; WHILE a condition is True we iterate something, Else IF it's False, we exit the loop.

name = input("Enter your name: ")

# An If statement executes once and continue to the rest of the program
if name == "":
    print("You did not enter your name...")
else:
    print(f"Hello {name}!")

# A While loop repeats (iterates) while a condition is True...
while name == "":
    print("You did not enter your name...")
    name = input("Enter your name: ")
# The While loop continues when the condition is False
print(f"Hello again {name}!")

# Be sure to include a way to escape lest you get stuck in an infinite loop

age = int(input("Enter your age: "))

# Like with If staements, you can include parentheses for readability
while (age < 0):
    print("ERROR: Inavlid Input - Age cannot be negative.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# You can introduce logical operators within the condition
food = input("Enter your favorite food (q to quit): ")

while not (food == "q"):
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")
print("Exiting While Loop...")

num = int(input("Enter a number between 1-10: "))
# The condition num < 1 or num > 10 can be replaced by 10 > num > 1
while (num < 1 or num > 10):
    print(f"ERROR: Inavlid Input - Number must be within range 0 - 10.")
    num = input("Enter a number between 1-10: ")
print(f"Your number is {num}.")