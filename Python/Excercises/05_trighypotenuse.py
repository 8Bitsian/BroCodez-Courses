# Project 04: Hypotenuse Calculator - Uses Note 4
# Calculate the hypotenuse of a right triangle by importing the math library

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# Equation for the hypotenuse of a right triangle c = a² + b²
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

# Use the round function to round to two decimal places
print(f"The hypotenuse (side C) is: {round(hypotenuse, 2)}cm")
