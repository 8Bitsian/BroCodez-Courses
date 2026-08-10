# Iterables

# An iterable is an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# Lists are considered iterable since we can use them in loops
numbers = [1, 2, 3, 4, 5]

# The counter variable should be named to according to what's being counted for readability
for number in numbers:
    # The keyword end replaces the newline character at the end of each line
    print(number, end=" ")  # Prints "1 2 3 4 5 "
print()

# You can iterate a list backwards w/the reversed() method
for number in reversed(numbers):
    print(number, end=" ")  # Prints "5 4 3 2 1 "
print()

# Tuples are also iterable and reversable
letters = ("A", "B", "C", "D", "E")
for letter in letters:
    print(letter, end=" ")  # Prints "A B C D E "
print()

for letter in reversed(letters):
    print(letter, end=" ")  # Prints "E D C B A "
print()

# Sets are iterable but they are not reversable: Will receieve a "TypeError" message "'set' object is not reversable"
fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit, end=" ")   # Prints "apple orange banana coconut"
print()

# Strings are special list arrays, so they are iterable via indicies
name = "8Bit Software"
for character in name:
    print(character, end=" ")
print()

# Dictionaries are iterable
my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

for key in my_dictionary:
    print(key, end=" ")
print()

for value in my_dictionary.values():
    print(value, end=" ")
print()

# Print key and value on the same line only use item as counter
for item in my_dictionary.items():
    print(item, end=" ")
print()

# Print key and value on new lines use ke yand value as counter
for key, value in my_dictionary.items():
    print(f"{key} = {value}")
print()