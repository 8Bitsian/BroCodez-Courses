# Typecasting - Typecasting is the process of converting a variable from one data type to another.
# There are four different functions [@BroCodez](https://www.youtube.com/watch?v=ix9cRaBkVe0) will discuss:
# 1. str():
# 2. int():
# 3. float():
# 4. bool():

name = "Imani Holle"
age = 23
gpa = 3.2
is_student = True

# This will print what datatype the variable is
print(type(name))       # "<class 'str'>"
print(type(age))        # "<class 'int'>"
print(type(gpa))        # "<class 'float'>"
print(type(is_student)) # "<class 'bool'>"

# you can convert the gpa to an integer
gpa = int(gpa)
print(gpa) # The decimal portion will be truncated and will print "3"

# you can convert the age to a string
age = str(age)
print(type(age)) # Will appear the same, but it's a string now
# age += 1 now will give an error

name = bool(name)
print(name) # Typecasting text will give True unless there is nothing "" then its False