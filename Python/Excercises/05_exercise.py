# Exercise 05: Cacluate the Hypotenuse of a Right Triangle
# 4 Notes

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# Equation for the hypotenuse of a right triangle c = a² + b²
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

# Use the round function to round to two decimal places
print(f"The hypotenuse (c) is: {round(hypotenuse, 2)}cm")