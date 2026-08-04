# Exercise 09: Password Checker - Validate user input with the following requirements.
# 7-8 Notes

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
