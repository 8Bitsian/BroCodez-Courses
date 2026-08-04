# Logicial Operators - A logical operator evaluates multiple conditions (like the comparision operators) with boolean logic
# There are three different logical operators [@BroCodez](https://www.youtube.com/watch?v=ix9cRaBkVe0) will discuss:
# 1. Or: ONE of the conditions must be True
# 2. And: BOTH of the conditions must be True
# 3. Not: Inverts the conditions (NOT False or NOT True)

temp_check = 30
is_raining = False

# With the or logical operator, ONE of the conditions must be True for the if statement to execute
if (temp_check > 25 or temp_check < 0 or is_raining):
	# Because the temp is greater than 25, the statement will print
	print("The event is canceled.")
else:
	print("The event is scheduled.")
	
temp = 28
is_sunny = True

# With the and logical operator, ALL of the conditions must be True for the if statement to execute
if (temp >= 28 and is_sunny):
	# Because the temp is less than 28 AND it's sunny, the statement will print
	print("It is HOT outside. 🥵")
	print("It is SUNNY outside. ☀️")
elif (tempo <= 0 and is_sunny):
	#Because the temp is less than 0 AND it's sunny, the statement will print
	print("It is COLD outside. 🥶")
	print("It is SUNNY outside. ☀️")
elif (28 > temp > 0 and is_sunny):
	# To check for a certain range, you can simplify chained comparisions
	# temp < 28 and temp > 0 is the same as 28 > temp > 0
	print("It is WARM outside. 😎")
	print("It is SUNNY outside. ☀️")
elif (temp >= 28 and not is_sunny):
	# You can invert to check for an opposite state using the Not operator
	# this will check if it is not sunny (i.e., cloudy)
	print("It is HOT outside. 🥵")
	print("It is CLOUDY outside. ☁️")
elif (tempo <= 0 and is_sunny):
	print("It is COLD outside. 🥶")
	print("It is CLOUDY outside. ️️️☁️")
elif (28 > temp > 0 and is_sunny):
	print("It is WARM outside. 🙂")
	print("It is CLOUDY outside. ☁️")
