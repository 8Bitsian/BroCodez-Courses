# For Loops - A basic form of decision making; WHILE a condition is True we iterate something a given number of times, Else IF it's False, we exit the loop.

# For loop will execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.
# Syntax for for clause is "for counter in range(start, end)"
# End is exclsuive, so add one when wanting to include in range
for x in range(1, 11):
	print(x)	# Prints "1 2 3 4 5 6 7 8 9 10" on newlines

# To count backwards use the reversed function
for x in reversed(range(1, 11)):
	# The following print function is inside of the for loop so it iterates 10 times
	print(x)	# Prints "10 9 8 7 6 5 4 3 2 1"
# The following print function is outside of the for loop so it prints once
print("HAPPY NEW YEAR!")

# You can step with the optional parameter in the range function
for x in range(1, 11, 2):
	# The step parameter begins at index 0 (in this case 1)
	print(x)	# Prints "1 3 5 7 9"
	
# Because the for loop is capable of indexing we can splice strings
credit_card = "1234-5678-9012-3456"
  # position = 0123456789012345678 (19 indexes(characters))

for x in credit_card:
	# The start parameter begins at index 0 (in this case 1)
	print(credit_card) # Prints "1 2 3 4 - 5 6 7 8 - 9 0 1 2 - 3 4 5 6"
	
# The following keywords are also available for the while loop: break and continue

# The continue keyword stays within the same decision logic (i.e., if-else statement)
for x in range(1, 10):
	if x == 7:
		# This skips over the index matching the value of "7"
		continue
	else:
		print(x)	# Prints "1 2 3 4 5 6 8 9 10" on newlines

# The break keyword leaves the decision logic
for x in range(1, 10):
	if x == 7:
		# This stops at the index matching the value of "7"
		break
	else:
		print(x)	# Prints "1 2 3 4 5 6 7" on newlines

	
