# Exercise 08: Temperature Converter - Create a temperature converted using an if statement
# 5 Notes

unit = input("Celcius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: ")

if unit == "C":		# C -> F
	f_temp = (temp * (9.0 / 5.0)) + 32.0
	unit = "°F"
	print(f"The temperature is: {round(f_temp, 3)} {unit}")
elif unit == "F":	# F -> C
	c_temp = (temp - 32.0) * (5.0 / 9.0)
	unit = "°C"
	print(f"The temperature is: {round(c_temp, 3)} {unit}")
else:	# Error message
	print(f"{unit} was not a valid unit of measurement")
