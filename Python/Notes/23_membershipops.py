# Membership Operators

# Membership operators are used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)

# the following are considered membership operators:
# `in`: 
# `not in`:

secret_word = "APPLE"

letter = input("Guess a letter in the secret word: ")

# The `in` keyword will return a boolean value of `True` or `False`
if letter in secret_word:
    print(f"There is a {letter}.")
else:
    print(f"{letter} was not found.")

# Lists, tuples, and sets behave similarly
students = {"Farland", "Lena", "Lousie"}

student = input("Enter the name of a student: ")

# Using the `not` keyword would reverse the resting state
if student not in students:
    print(f"{student} was not found.")
else:
    print(f"{student} is a student.")

grades = {"Farland": "A",
          "Lena": "B",
          "Lousie": "C"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"{student} was not found.")

email = "8BitSoftware@website.com"

# Can check multiple conditions
if "@" in email and "." in email:
    print(f"{email} is a valid email.")
else:
    print(f"{email} is an invalid email.")