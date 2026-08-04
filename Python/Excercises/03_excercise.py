# Exercise 03: Cacluate the Circumference of a Circle
# 4 Notes

import math

radius = float(input("Enter the radius of a circle: "))

# Equation for the circumference of a circle C = 2πr
circumference = 2 * math.pi * radius

# Use the round function to round to two decimal places
print(f"The circumference is: {round(circumference, 2)}cm")