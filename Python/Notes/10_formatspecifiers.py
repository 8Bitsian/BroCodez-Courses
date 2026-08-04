# Format Specifiers - Format specifiers are {value:flags} that format a value based on what flags are inserted.

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 12345.78
price5 = 1987456.3215

# The :.(num)f specifier rounds to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.2f}") # Prints "Price 1 is $3.14"

# The :(num) specifier allocates that many spaces as a buffer
print(f"Price 2 is ${price2:10}")  # Prints "Price 2 is $-   987.65"

# The :0(num) specifier allocates and zero-pads that many spaces
print(f"Price 3 is ${price3:010}") # Prints "Price 3 is $0000012.34"

# The :<(num) specifier left justifies using the left angle bracket
print(f"Price 1 is ${price1:<10}") # Prints "Price 1 is $3.14159   "

# The :>(num) specifier right justifies using the right angle bracket
print(f"Price 2 is ${price2:>10}") # Prints "Price 2 is $   -987.65"

# The :^(num) specifier center aligns
print(f"Price 3 is ${price3:^10}") # Prints "Price 3 is $  12.34   "

# The :+ specifier indicates a positive value
print(f"Price 1 is ${price1:+}")   # Prints "Price 1 is $+3.14159"

# The ": "  specifier inserts a space before positive numbers
print(f"Price 1 is ${price1: }")    # Prints "Price 1 is $ 3.14159"

# The :- specifier indicates a negative value
print(f"Price 1 is ${price1:-}")    # Prints "Price 1 is $-3.14159"

# The :, specifier inserts a comma before numbers
print(f"Price 4 is ${price4:,}")    # Prints "Price 4 is $12,345.78"

# We can mix and match flags for better readbility
# The sytax for formatting specifiers are {var: [fill][align][sign][#][0][width][,][precision][type]}
print(f"Price 5 is ${price5:>15,.2f}") # Prints "Price 5 is $   1,987,456.32."