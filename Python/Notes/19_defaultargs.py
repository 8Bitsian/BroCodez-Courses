# Default Arguments

# A default argument is a default value for certain paramters
# The default is used when that argument is omitted and makes your functions more flexible, and reduces the number of arguments

# @BroCodez goes over four types of default arguments, but has covered two so far: (1) Positional arguments are used when initializing functions and (2) DEFAULT arguments

# When calling function you can set positional paramters by sending them as arguments
# print(net_price(950, 0, 0.05))

# To pass DEFAULT arguments initialize them in the function definition
# DEFAULT arguments are best for known base values
def net_price(list_price, discount = 0.0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

# You don't have to pass default arguments
print(net_price(950))

print(net_price(950, 0.1))

print(net_price(950, 0.1, 0))