# String Indexing - Accessing elements of a string, or sequence, using [start : end : step] (indexing operator)

# Indexes start at 0 because computers start there and continues onwards.
credit_number = "1234-5678-9012-3456"
    # position = 0123456789012345678 (19 characters)

# There is up to three fields you can fill in with the indexing operator:
# If you put an index with no colon it's assumed you're refered to the start positions
print(credit_number[0])     # Prints "1"

# To print a range you have to use a colon and the ending index
# The ending index is exclusive to whatever your ending point it will show one less character
print(credit_number[0:5])   # Prints "1234-"

# You can omit 0 since the starting index is inclusive and assumes that as a starting point
print(credit_number[:4])    # Prints "1234"

print(credit_number[5:9])   # Prints "5678"

# To print to the end of the string put the starting index and a colon
print(credit_number[5:])    # Prints "5678-9012-3456"

# To print the last set of digits, the indexing position can be referenced in reverse
# Remember that the negative inital starting point starts at -1 and not 0
# credit_number = "1234-5678-9012-3456"
    #   position = 9876543210987654321 (19 characters)

print(credit_number[-1])  # Prints "6"

# Using the step field, we can access characters in increments of a given value instead of one by one
# To parse the entire string we put two colons since Python will assume from index 0 to the end of the string

# credit_number = "1234-5678-9012-3456"
    #   position = P-P-P-P-P-P-P-P-P-P (every 2nd character)
print(credit_number[::2])   # Prints "13-6891-46"

# credit_number = "1234-5678-9012-3456"
    #   position = P--P--P--P--P--P--P (every 3rd character)
print(credit_number[::3])   # Prints "146-136"

# To reverse a string set the step to be negative
# credit_number = "1234-5678-9012-3456"
    #   position = 9876543210987654321 (19 characters)
print(credit_number[::-1])  # Prints "6543-2109-8765-4321"