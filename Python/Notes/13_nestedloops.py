# Nested Loops - A loop within another loop (outer and inner)

# Nested loop syntax:
# Outer loop: (The loop on the outer most part of the decision structure)
    # The inner loop is always indented as it's considered part of the block of code
    # Inner loop: (The loop on the inner most part of the decision structure)

# You can have a variety of nested loops (ex. while inside of while, for inside of for, etc.)

# Remember that the end index is exclusive so the rnage is 1-9 not 10
for x in range(1, 4):
    # Each print statement ends w/a new line escape character
    print(x)    # Prints each # with "\n" implicitly "1 2 3"
    # This is the same as: print(x, end="\n")

for x in range(1, 4):
    # To print everything on the same line, use the end specifier with an empty string
    print(x, end="")  # Prints "123"
print()

for x in range(1, 4):
    # You can add anything within the end line specifier, like a space (" ")
    print(x, end=" ")   #Prints "1 2 3"
print()

# To iterate a loop, nest the loop within the code block of another loop
for x in range(3):  # Outer loop iterates the inner loop x number of times
    # The inner loop counter must be different from the outer loop
    for y in range(1, 10):  # Inner loop iterates y number of times
        print(y, end=" ")   # Prints y value x times (y * x)
    # You can continue working within the outer loop by outdenting
    # To print each iteration on a separate line write a blank print statement
    print() # Prints a new line
# The following  print statement is considered outside of the nested loop
# You can calculate the amount of iterations by multiplying the counter variables
# Be sure to add 1 to the outer loop to because it is exclusive
print((x + 1) * y)    # Prints "27"

# Ex. Creates a rectangle of symbols
rows = int(input("Enter # of rows: "))
cols = int(input("Enter # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end="")
    print()