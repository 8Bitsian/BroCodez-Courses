# Exercise 07: Weight Converter - Create a weight converted using an if statement
# 5 Notes

weight = float(input("Enter your weight: ")
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":		# Kgs -> Lbs
	weight *= 2.205
	unit = "Lbs."
	print(f"Your weight is: {round(weight, 3)} {unit}")
elif unit == "L":	# Lbs -> Kgs
	weight /= 2.205
	unit = "Kgs."
	print(f"Your weight is: {round(weight, 3)} {unit}")
else:
	print(f"{unit} was not valid")
