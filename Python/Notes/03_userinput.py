# User Input - We can accept user input using the input function which prompts the user to enter data and returns entered data as a string

# Instead of having a sepearte print function, within the input function type a string to prompt the user
# You can assign the value to a variable using an assignment operator
name = input("What is your name? ")

# In order to alter the user input in an expression, you have to typecast since it's a string
# age = input("How old are you? ")
# age = int(age)
# age += 1

# You can use fewer lines when typecasting to save space and for readability
age = int(input("How old are you? "))
age += 1

# Only use a printf string if you want to insert variables
print(f"Hello {name}!")
print("Happy birthday!")
print(f"You are {age} years old.")