# Variables - A variable is a container for a value - like a box. A variable behaves as if it were the value it contains.
# There are four different data types [@BroCodez](https://www.youtube.com/watch?v=ix9cRaBkVe0) will discuss:
# 1. Strings: A series of unique characters
# 2. Integer: A whole number
# 3. Floats: A floating-point number, a number with a decimal portion
# 4. Boolean: Hold the expression true or false

# These are strings being directly printed to the console
print("I like pizza!")
print("It's really good.")

# The following are variables with string datatypes using the printf statement
first_name = "Imani Hollie"
print(first_name)
print(f"Hello {first_name}!")

food = "pizza"
print(f"You like {food}.")

email = "IHollie123@website.com"
print(f"Your email is: {email}")

# The following are variables with integer datatypes using the printf statement
age = 23
print(f"You are {age} years old.")

itmes = 3
print(f"You are buying {items} items.")

num_of_students = 30
print(f"your class has {num_of_students} students.")

# The following are variables with floating-point datatypes using the printf statement
price = 10.99
print(f"The price is: ${price}")

gpa = 3.2
print(f"Your GPA is: {gpa}")

distance = 5.5
print(f"You ran {distance} kilometers.")

# The following are variables with boolean datatypes using the printf statement
# Booleans can only be one of two states: True or False (must be capitalized)
is_student = True
print(f"Are you a student?: {is_student}?")

# Booleans are often used in if statements (decision structures)
is_worker = True
if is_worker: # If true...
    print("You are an employee.")
else: # If false...
    print("You are unemployed.")

for_sale = False
if for_sale: # If true...
    print("That item is for sale.")
else: # If false...
    print("That item is not available.")

is_online = True
if is_online: # If true...
    print("You are online.")
else: # If false...
    print("You are offline.")