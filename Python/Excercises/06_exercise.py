# Exercise 06: Cacluator Program - Create calculator using the if statement decision structure
# 4-5 Notes

operator = input("Enter Operator (+ - * ** / %): ")

# You have to typecast the input functions as floats
num1 = float(input("Enter the 1st number: ")
num1 = float(input("Enter the 2nd number: ")

if (operator == "+"):
	# Addition (use the round function for two decimal places)
	add = num1 + num2
	print(f"{num1} + {num2} = {round(add, 2)}")
	# You can include the keywords "pass" as a placeholder
elif (operator == "-"):
	# Subntraction
	sub = num1 - num2
	print(f"{num1} - {num2} = {round(sub, 2)}")
elif (operator == "*"):
	# Multiplication
	mul = num1 * num2
	print(f"{num1} * {num2} = {round(mul, 2)}")
elif (operator == "**"):
	# Exponentiation (use the pow function for readability)
	exp = pow(num1, num2)
	print(f"{num1} ** {num2} = {round(exp, 2)}")
elif (operator == "/"):
	# Division
	div = num1 / num2
	print(f"{num1} / {num2} = {round(div, 2)}")
elif (operator == "%"):
	# Modulus (remainder)
	mod = num1 % num2
	print(f"{num1} % {num2} = {round(mod, 2)}")
else:
	# Default statement for invalid options
	print(f"ERROR: Invalid Input - {operator} is not available")
