# String Methods - A string is a series of characters

name = input("Enter your full name: ")
# Example: imani Hollie
# Pos:     012345678901 (12)

# The length function returns an integer of however many characters are within a string
result = len(name)
print(result) # Will print "12" becauses it includes spaces

# The find method will return the first occurance (position or index) of a given character
# When working with indexes we always begin with 0
result = name.find("i")
print(result) # Will print "0"

# The reverse find (hence rfind) method will return the last occurance (position or index) of a given character
result = name.rfind("i")
print(result) # Will print "10"

# If either method cannot find anything, then it will return "-1"
result = name.rfind("z")
print(result) # Will print "-1"

# The capitalize method will change the case of the first character within a string, which will then return a string
name = name.capitalize()
print(name) # Will print "Imani Hollie"

# The upper method will change the case of the all of the characters within a string to be uppercase, which will then return a string
name = name.upper()
print(name) # Will print "IMANI HOLLIE"

# The lower method will change the case of the all of the characters within a string to be lowe4rcase, which will then return a string
name = name.lower()
print(name) # Will print "imani hollie"

# The is digit method will return a boolean of True if the string contains only digits (0-9), or False otherwise
result = name.isdigit()
print(result) # Will print "False" even with mixed letter and numbers

# The is alpha method will return a boolean of True is the string contains only alphabetical characters (a-z or A-Z), or False otherwise
result = name.isalpha()
print(result) # Will print "False" because a space " " isn't considered an alphabetical character

phone_number = int(input("Enter your phone number: "))
# Example: 1-123-456-7890
# Pos    : 01234567890123 (14)

# The count method will return the number of instances of however many times it appears within a string
result = phone_number.count("-")
print(result) # Will print "3"

# The replace method will replace a specified character by another given character
phone_number = phone_number.replace("-", " ")
print(phone_number) # Will print "1 123 456 7890"

# You can also replace it with an empty string
phone_number = phone_number.replace("-", "")
print(phone_number) # Will print "11234567890"

# To get a list of all string method available top you, use the help function with the string datatype
print(help(str))
