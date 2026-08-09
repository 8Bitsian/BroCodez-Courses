# Exercise 12: Count Up Timer - Display a timer
# 19 Notes

# Import the time module for .sleep() method
import time

# Define function for timer
# def count(start = 0, end) will give SyntaxError since non-default arguments must follow default arguments
def count(end, start = 0):
    # The end index in the range() method is exclusive, so add 1 to include in range
    # The start index in the range() method is initialized to 0
    for x in range(start, end + 1):
        print(x)
        # The .sleep() method uses seconds as time interval
        time.sleep(1)
    print("DONE!")
    print()

# Start index is intialized to 0, and passes value to end index 
count(3)

# Passes 6 to end index, and 3 to start index
count(6, 3)