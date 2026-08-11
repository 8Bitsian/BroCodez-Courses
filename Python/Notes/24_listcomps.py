# List Comprehensions

# List comprehensions are a concise way to create lists in Python
# They are more compact and easier to read than traditional loops

doubles = []
for x in range(1, 6):
    doubles.append(x * 2)
print(doubles)  # Prints "[2, 4, 6, 8, 10]"

# The following list comprehension is the same as the block above
# [(expression) `for` value `in` iterable `if` (condition)]
doubles = [(x * 2) for x in range(1, 6)]
print(doubles)  # Prints "[2, 4, 6, 8, 10]"

triples = [(x * 3) for x in range(1, 6)]
print(triples)  # Prints "[3, 6, 9, 12, 15]"

squares = [(x * x) for x in range(1, 6)]
print(squares)  # Prints "[1, 4, 9, 16, 25]"
print()