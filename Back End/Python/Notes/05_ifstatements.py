# If Statements: A basic form of decision making; IF a condition is True we do something, Else If it's False, we do something else.

age = int(input("Enter your age: "))

# We can use if statemnts to check conditions
if age >= 100: # Greater than or equal to
	# Be sure that code underneath the initial if statement is indented
	print(f"Becuase you are {age}, you are an elder.")
elif age >= 18:
	# You can check multiple conditions with the if else statement
	print(f"Becuase you are {age}, you are an adult.")
elif age >= 17:
    # Another way to write the if else statement is with elif
    print(f"Becuase you are {age}, you are a child.")
elif (age <= 0): # Less than or equal to
    # You don't have to use parentheses, but it makes it easier for readability
    print(f"You haven't been born yet!.")
else:
    # The Else statement is a last resort or considered the "default option"
    # If the previous coditions are false then we are directed here
    print("You must be 18+ to sign up")
    
reponse = input("Would you like to order? (Y/N): ")

# One equal is the assignment operator, two equals is the equal to, or comparison, operator
if reponse == "Y":
	print("Have some food!")
else: # response == "N":
	print("No thank you.")
	
name = input("Enter your name: ")
if name == "":
	print("You did not respond.")
else:
	print(f"Hello {name}!")

# Boolean can be used in placed of a condition since with the if statement it would evaluate to True or False
for_sale = True
if for_sale: # True
	print("This item is for sale.")
else: # False
	print("This item is NOT for sale.")
	
is_online = False
if is_online: # True
	print("This user is online.")
else: # False
	print("This user is offline.")
