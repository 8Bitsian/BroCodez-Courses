# Exercise 04: Cacluate the Area of a Circle
# 4 Notes

import math

radius = float(input("Enter the radius of a circle: "))

# Equation for the area of a circle A = πr²
area = math.pi * pow(radius, 2)

# Use the round function to round to two decimal places
print(f"The area is: {round(area, 2)}cm²")