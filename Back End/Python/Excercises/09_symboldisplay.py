# Exercise 09: Rectangle Symbol Display - Notes 10-13
# Display a rectangle made of symbols using nested loops and format specifiers

rows = int(input("Enter # of rows: "))
cols = int(input("Enter # of columns: "))
symbol = input("Enter a symbol to use: ")

# Ex. Creates a rectangle of symbols
for x in range(rows):
    for y in range(cols):
        print(symbol, end="")
    print()
