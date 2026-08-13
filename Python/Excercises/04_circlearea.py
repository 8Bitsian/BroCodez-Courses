# Project 04: Circle Area Calculator - Uses Note 4
# Calculate the circumference of a circle by importing the math library

import math

radius = float(input("Enter the radius of a circle: "))

# Equation for the area of a circle A = πr²
area = math.pi * pow(radius, 2)

# Use the round function to round to two decimal places
print(f"The area is: {round(area, 2)}cm²")
