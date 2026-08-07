# 2D Collections - A two-dimensional list[] is a list made up of lists

# You can also create 2D tuples()
# This is useful for when you are working with matrices or grids of data
# It is similar to an excel spreadsheet

# Still following the same naming convensions for 1D lists
fruits = ["apple", "orange", "banana", "coconut"]
vegatables = ["celery", "carrot", "potato", "brocolli"]
meats = ["chicken", "steak", "fish", "lamb"]

# To create a 2D list, you can think of it like nested loop, create a 1D list first, then "nest" the other 1D lists within the elements of the "outer" list
groceries = [fruits, vegatables, meats]

# To print the elements within a 1D list, put the name of the list in a print() function
print(fruits)       # Prints "['apple', 'orange', 'banana', 'coconut']"

# To print a specific element from within the list, reference it with its index position, starting from 0
print(fruits[3])    # Prints "coconut"

# To change the value of an element in a 1D list, use an assignment operator (=) w/the index of the element you want to acess
fruits[3] = "strawberry"
print(fruits)       # Prints "['apple', 'orange', 'banana', 'strawberry']"

# If I were to print the 2D list w/out formatting, it would print every list separated by commas within a square bracket on one line
print(groceries)    # Prints "[fruits[], vegatables[], meats[]]"
print()
# The 2D list can be parsed similar to that of a grid, w/1D list names as rows and elements as columns
# Like a 1D list to reference a element (which is an entire list), use the index starting from 0
print(groceries[0]) # Prints fruits list:     "['apple', 'orange', 'banana', 'strawberry']"
print(groceries[1]) # Prints vegatables list: "['celery', 'carrot', 'potato', 'brocolli']"
print(groceries[2]) # Prints meats list:      "['chicken', 'steak', 'fish', 'lamb']"
print()

# To access an element found within one of the rows (list), you need to reference that specific index too
# you can think of this system like coordinates on a grid
print(groceries[1][0])  # Prints element 0 from vegatables list: "celery"
print(groceries[0][1])  # Prints element 1 from vegatables list: "orange"
print(groceries[2][2])  # Prints element 2 from vegatables list: "fish"
print()

# Like with 1D lists, if you try to access an indices out of range, you will get the 'IndexError'

# To print entire lists from within a 2D list, use loops
# To iterate over the elements within lists of a 2D list, use nested loops
for list in groceries:
    for food in list:
        print(food) # Prints individual items of each list on every new line
print()

# To iterate over the elements within lists of a 2D list, use nested loops
for list in groceries: # rows
    for food in list:   # coloums
        print(food, end=" ") # Prints individual items of each list on every newline
    print()
print()

# You can mix and match different types of collections within 2D lists

# It isn't necessary to give the elements within a 2D names, but it is great for readability
numbers = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]

print(numbers[0])
print(numbers[1])
print(numbers[2])