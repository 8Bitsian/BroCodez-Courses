# Exercise 09: Number Pad display - Display a number pad using a tuple and 2D arrays
# 14-15 Notes

# We'll use a tuple() since the data being displayed will not change and it's faster

# Put rows on newlines for better readability
num_pad = (("1", "2", "3"),
           ("4", "5", "6"),
           ("7", "8", "9"),
           ("*", "0", "#"))

# This would print every tuple w/parentheses
# for row in num_pad:
#    print(row)

# This would print every tuple w/out parentheses
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()