# The addition operator adds value to another value
freinds = friends + 1
print(friends) # Will print "6"
# An augmented assignment operator is just a condensed version of the expanded operator
friends += 1
print(freinds) # Will print "7"

# The subtraction operator subtracts value from another value
freinds -= 2
print(freinds) # Will print "5"

# The multiplication operator multiplies value to another value
freinds *= 5
print(freinds) # Will print "25"

# The exponentiation operator raises value to another value
freinds **= 2
print(freinds) # Will print "50"

# If you indend to have integers, you will either have to typecast to prevent splitting people in two
freinds /= 2
print(freinds) # Will print "25"

# Or you will have to use modulus which gives the remainder. Think of splitting off into groups and counting the stragglers
# Modulus is great at finding if a number is even or odd by using 2 and sending back however many are left
remainder = freinds % 2
print(remainder) # Will print "1"

x = 3.14
y = -4
z = 5

# The basic most funtions included without needing to import the math library include: 
# The round function will print the nearest whole integer
result = round(x) # Will print "3"

# The absolute value function will print the distance away from zero
result = abs(y) # Will print "4"

# The power function will raise the base (4) to a given power (z)
result = pow(4, z) # Will print "1024"

# The maximum function will print the max value of any given values
result = max(x, y, z) # Will print "5"

# The minimum function will print the min value of any given values
result = min(x, y, z) # Will print "-4"

# From here onwards, you'll have to import the math library to get access to these functions
import math

# The value of PI (3.14159...)
print(math.pi)

# The constant E (2.71828...)
print(math.e)

# The square root function will print the sqrt of the base
result = math.sqrt(25) # Will print "5"

# The ceiling function will always round a floating-point number up to the next integer
result = math.ceil(x) # Will print "4"

# The floor function will always round a floating-point number down to the next integer
result = math.floor(x) # Will print "3"