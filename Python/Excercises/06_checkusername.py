# Exercise #06: Username Checker - Uses Notes 5-8
# Validate user input w/if statements using logical operators in the conditions.

username = input("Enter a username: ")

# 1. Username is no more than 12 characters
if len(username) > 12:
	print("ERROR: Invalid Input: Username is longer than 12 characters.")
# 2. Username must not contain spaces
elif not username.find(" ") == -1:
	print("ERROR: Invalid Input: Username cannot contain spaces.")
# 3. Username must not contain digits
elif not username.isalpha(): # Will also check for spaces
	print("ERROR: Invalid Input: Username cannot contain digits.")
else:
	print(f"Welcome {username}")
