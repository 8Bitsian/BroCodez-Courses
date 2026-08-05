# Project 06: Countdown Timer Program - Create a countdown timer using a for loop
# Use 12 Notes
# Create a for loop with an if-elif statement for a counter

# Import the time module to get access to the sleep() function
import time

my_time = int(input("Enter the time in seconds: "))

# Using a negative number in the step interval is the same as using the reversed function
for x in (range(my_time, 0, -1)):
	seconds = x % 60
	minutes = int(x / 60) % 60
	hours = int(x / 3600) # would include "% 24" if there were days
	# x acts as our counter
	print(f"{hours:02}:{minutes:02}:{seconds:02}") # Prints "00:00:00"
	# sleep() function uses seconds as time interval
	time.sleep(1)

# Prints after 3 seconds
print("Time's Up!")
