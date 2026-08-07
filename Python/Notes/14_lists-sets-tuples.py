# Lists, Sets, and Tuples - Collections are single "variable" used to store multiple values

# There are 4 general purpose collections, but @BroCodez discusses 3:
# 1. var[]: Lists use brackets and are ordered and changeable.
# - Duplicates OK
# 2. var{}: Sets use curly braces and are unordered and immutable.
# - Add/Remove OK. NO duplicates
# 3. var(): Tuples use parentheses and are ordered and unchangeable.
# - Duplicates OK. FASTER because data is in fixed positions

# Variables only store one value to memeory
fruit = "apple"
print(fruit)    # Prints "apple"

# Collections are able to store multiple values to memory via indices
# Lists surround thier values with a square bracket ([]) and separate them with a comma (,)
# Note: A naming convention for collections is to make the variable names plural since they are storing multiples of related values
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)   # Prints "['apple', 'orange', 'banana', 'coconut']"

# To access elements within the collection, refer to their index position liek with string splicing
# The values are stored with the starting index at 0
print(fruits[0])    # Prints "apple"
print(fruits[1])    # Prints "orange"
print(fruits[2])    # Prints "banana"
print(fruits[3])    # Prints "coconut"

# If you reference an element out of the range, you will get an error message called IndexError

# Like with a string, you can splice your list by setting a start index, end index, and step index
# To print a range, you can use the end index to print from the start index to one less than the given index since the end index is exclusive
print(fruits[:3])   # Prints "['apple', 'orange', 'banana']"
# To print every other index, you can use the step index
print(fruits[::2])  # Prints "['apple', 'banana']"
# To print the entire list backwards, you can use -1 in the step index to decrement
print(fruits[::-1]) # Prints "['coconut', 'banana', 'orange', 'apple']"

# You can iterate over collections with loops
# Note: Another naming convention dictates that you can use a singluar version of the word for your collection, since that's what it would be counting. This helps with readability
for fruit in fruits:    # Instead of x put fruit
    print(fruit)    # Prints each index on a newline

# To list the different methods available to collections use a print statement witrh the the directory function dir(val)
# print(dir(fruits))  # Prints list of availble attributes and methods in alphabetical order
# To get a description of each of the methods listed, use the help function help(var)
# print(help(fruits)) # Prints descriptions of available methods

# To get the number of indices within a collection, use the length function
print(len(fruits))  # Prints "4"

# If you add another value, the number of indices increases by the amount of newly added values
fruits = ["apple", "orange", "banana", "coconut", "pineapple"]
print(len(fruits))  # Prints "5"

# Using the in operator, you can parse a collection for a specific value and get a boolean (either True or False)
print("apple" in fruits)    # Prints "True"
print("cherry" in fruits)   # Prints "False"

# Because lists are ordered and changeable, we can change the values of indices
fruits[0] = "cherry"
for fruit in fruits:
    print(fruit)    # Prints "['cherry', 'orange', 'banana', 'coconut', 'pineapple']"

# There are a few specific methods that can be used w/lists
# The .append(var) method adds values to the end of the list
fruits.append("apple")
print(fruits)   # Prints "['cherry', 'orange', 'banana', 'coconut', 'pineapple', 'apple']"

# The .remove(var) method removes values from any index within the list
fruits.remove("banana")
print(fruits)   # Prints "['cherry', 'orange', 'coconut', 'pineapple', 'apple']"

# The .insert(pos,var) method adds values to any index within the list
fruits.insert(2, "blackberry")
print(fruits)   # Prints "['cherry', 'orange', 'blackberry', 'coconut', 'pineapple', 'apple']"

# The .sort(list) method will sort a list in ascending alphabetical order
fruits.sort()
print(fruits)    # Prints "['apple', 'blackberry', 'cherry', 'coconut', 'orange', 'pineapple']"

# The .reverse(list) method  will sort a list in descending numerical order based on their indices
# The .reverse(list) method right after the .sort() method will sort a list in descending alphabetical order
fruits.reverse()
print(fruits)   # Prints "['pineapple', 'orange', 'coconut', 'cherry', 'blackberry', 'apple']"

# The .index(var) method will return the numerical index positon of an element
print(fruits.index("apple"))    # Prints "5"
# If there isn't a value you will get an Error message for a ValueError

# The .clear() method will delete any elements within the list
fruits.clear()
print(fruits)   # Prints "[]"

# The .count(var) method will count the number of instances of a value within your list
# This is possible because duplicates are able to exist within lists
fruits = ["apple", "apple", "apple"]
print(fruits.count("apple"))    # Prints "3"
# If no element is found with that specific value, then that index won't be counted
print(fruits.count("orange"))   # Prints "0"
print()

# Sets surround thier values with a curly brace and separate each with a comma `var{val1, ...}`.
# Sets are unordered and immutable (menaing we cannot change element values). Add/Remove OK (We can change their position). NO duplicates
# Since a set is unordered, when we print the set it will contain the same values but in a different position
colors = {"red", "green", "blue", "yellow"}
print(colors)         # Prints "{'blue', 'yellow', 'red', 'green'}"

# print(dir(colors))  # Prints list of availble attributes and methods in alphabetical order
# print(help(colors)) # Prints descriptions of available methods

print(len(colors))    # Prints "4"
print("purple" in colors)   # Prints "False"

# We cannot parse a set via indices since it's unordered. If we try anyways, we will get an error message called `TypeError`. Becuase of this we cannot change values within a set

# The .add(value) method allows us to append elements to the set
colors.add("purple")
print(colors)         # Prints "{'yellow', 'blue', `purple`, 'green', 'red'}" 

# The .remove(value) method allows us to delete elements from the set
colors.remove("green")
print(colors)         # Prints "{'red', 'blue', `yellow`, 'purple'}" 

# The .pop(value) method will delete whichever element is first, which because of the nature of set is random
colors.pop()
print(colors)         # Prints "{'purple', 'blue', 'red'}"

# The .clear() method will clear all elements within the set
colors.clear()
print(colors)         # Prints "set()"
print()

# Tuples surround thier values with parentheses and separate each with a comma `var(val1, ...)`.
# Tuples are ordered and unchangeable. Duplicates OK. FASTER because data is in fixed positions
times = ("morning", "day", "afternoon", "night")

# print(dir(times))  # Prints list of availble attributes and methods in alphabetical order
# print(help(times)) # Prints descriptions of available methods

print(len(times))    # Prints "4"
print("morning" in times)   # Prints "True"

# The .index(value) method will return the numerical index positon of an element
print(times.index("morning"))   # Prints "0"

# The .count(value) method will return the number of instances of a given value within the tuple
print(times.count("day"))   # Prints "1"
print(times.count("twilight"))   # Prints "0"

# Tuples are iterable over loops
for time in times:
    print(time) # Prints "morning day afternoon night"