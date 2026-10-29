# Project 05: Compound Interest Calculator - Create a calculator using an while loop
# 6-11 Notes
# Create a while loop with an if-elif statement for the user to calculate compound interest

# Interest is a charge for the privilege of borrowing money often expressed as USD
# and typically expressed as an Annual Percentage Rate (APR) calculated by: A = P (1 + (r/n)) ^t
# A = Final Amount
# P = Initial Principal Balance
# r = Interest Rate (expressed in float/decimal)
# t = number of time periods elapsed

principle = 0.0
rate = 0.0
time = 0

# Can use boolean to iterate while loop, be sure to inclue else clause to prevent infinite loop
while (True):
	principle = float(input("Enter the principle amount: $"))
	if principle < 0.0:
		print("ERROR: Invalid Input - Principle amount cannot be less than $0.00")
		principle = float(input("Enter the principle amount: $"))
	else:	# Keyword break will exit while loop
		break

# Can use a condition to iterate while loop
while (rate <= 0.0):
	rate = float(input("Enter the interest rate (as a decimal): "))
	if rate < 0.0:
		print("ERROR: Invalid Input - Interest rate cannot be less than or equal to 0.0%")
		rate = float(input("Enter the interest rate (as a decimal): "))

while (time < 0):
	time = int(input("Enter the elapsed amount of time in years: "))
	if time < 0:
		print("ERROR: Invalid Input - Elapsed time cannot be less than 0 years")
		time = int(input("Enter the elapsed amount of time in years: "))

apr = principle * pow((1 + (rate / 100)), time)

rate *= 100

print(f"Principle Balance: ${principle}")
print(f"Interest Rate: {rate}%")
print(f"APR after {time} years: ${apr:.2f}")
