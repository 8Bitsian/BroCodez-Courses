# Arbitrary Arguments

# Arbitrary refers to having to pass a varying amount of arguments, or when you aren't sure of how many will be passed through a function when invoked
# Arbitrary args. are prefixed w/the unpacking operator (`*`).
# There are two kinds of arbitrary args.:
# 1. `*args` allows you to pass multiple non-key arguments
# Non-key abritrary args. pack values within a tuple()
# 2. `**kargs` allows you to pass multiple keyword-arguments
# Keyword abritrary args. pack values within a dictionary{}

def subtract(a, b):
    return a - b

# Without arbitrary args. you would only be able to pass a set amount of args. defined previously in the function definition
print(subtract(1, 2))

# To have a function accept a varying amount of args, replace the args. in the function definition with the non-key argument
def add(*args):
    # The type(args) method will return a tuple of all of the arguments given
    # print(type(args))   # Prints "<class 'tuple'>"
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2))
print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("8", "Software")
display_name("8", "Bit", "Software")
display_name("Ms.", "8", "Bit", "Software")

# **kwargs allow you to pass multipel keyword arguments
def print_address(**kwargs):
    # The type(kwargs) method will return a tuple of all of the arguments given
    # print(type(kwargs)) # Prints "<class 'dict'>"
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "132 Fake St.",
              apt = "100",
              city = "Atlanta",
              state = "GA",
              zip = "86532")