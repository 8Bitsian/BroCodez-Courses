# If Statements: A basic form of decision making; IF a condition is True we do something, Else if it's False, we do something else.

age = int(input("Enter your age: "))

# We can use if statemnts to check conditions
if age < 13:
    # Be sure that code underneath the if statement is indented
    print(f"Becuase you are {age}, you are a child.")
if else age < 18:
    # You can check multiple conditions with the if else statement
    print(f"Becuase you are {age}, you are a teenager.")
elif age < 25:
    # Another way to write the if else statement is with elif
    print(f"Becuase you are {age}, you are a young adult.")
elif (age < 65):
    # You don't have to use parentheses, but it makes it easier for readability
    print(f"Becuase you are {age}, you are an adult.")
else:
    # The Else statement is a last resort
    # If the previous coditions are false then we are directed here
    print("You are an elder.")