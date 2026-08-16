# Setup
There are two things you need to download:
1. A Python Interpreter
- Go to [Python.org](https://www.python.org/) and download the latest version
2. An Integrated Development Environment (IDE)
- Go to [Jetbrains.com](https://www.jetbrains.com/pycharm/) and download the latest version of the community version (it's free :3)

# Variables
A variable is a container for a value - like a box. A variable behaves as if it were the value it contains.

There are four different data types [@BroCodez](https://www.youtube.com/watch?v=ix9cRaBkVe0) will discuss:
1. Strings: A `str` is a series of unique characters
2. Integer: An `int` is a whole number
3. Floats: A `float` is a floating-point number, or a number with a decimal portion
4. Boolean: A `bool` holds either the expression `True` or `False`

# Typecasting
Typecasting is the process of converting a variable from one data type to another.

There are four functions to convert a value or variable:
1. `str()`
2. `int()`
3. `float()`
4. `bool()`

# User Input
We can accept user input using the input function which prompts the user to enter data and returns entered data as a string.
Instead of having a sepearte print function, within the input function type a string to prompt the user you can asisgn the value to a variable using an assignment operator.

In order to alter the user input in an expression, you have to typecast since it's automatically a string. You can also save lines by typecasting prior to the `input()` within the same line to save space and for readability. 

You only need to use a printf string if you want to insert variables.

# Arithmetic & Math
## Arithmetic Operators
An augmented assignment operator is just a condensed version of the expanded operator.

| Operator | Example |
|:---|:---:|
| Addition: `+` | `var += num` |
| Subtraction: `-` | `var -= num` |
| Multiplication: `*` | `var *= num` |
| Exponentiation: `**` | `var **= num` |
| Division: `/` | `var /= num` |
| Modulus: `%` | `var %= num` |

## Built-in Math Functions
The basic most fuctions included without needing to import the math library include:
- `round(var)`: The round function will print the nearest whole integer
- `abs(var)`: The absolute value function will print the distance away from zero
- `pow(base, power)`: The power function will raise the base to a given power
- `max(var1, var2, var3, ...)`: The maximum value function will print the max value of any given values
- `min(var1, var2, var3, ...)`: The minimum value function will print the min value of any given values

## Imported Math Functions
From here onwards, you'll have to import the math library via: `import math` to get access to these functions
- `math.pi`: The value of constant PI (3.14159...)
- `math.e`: The value of constant E (2.71828...)
- `math.sqrt(var)`: The square root function will print the sqrt of the given value
- `math.ceil(var)`: The ceiling function will round a floating-point number up to the next integer
- `math.floor(var)`: The floor function will round a floating-point number down to the next integer

# Decision Structures
## If-statements
An if statement is a basic form of decision making; IF a condition is True we do something, Else If it's False, we do something else.

After the initial `if` statement be sure to indent the code that follows as Python doesn't use curely brakets.

We can use if statemnts to check conditions. When writing the conditions, it is best to use parentheses for readability.

| Condition | Example |
|:---|:---:|
| Greater Than: `>` | `var > value` |
| Less Than: `<` | `var < value` |
| Equal To: `==` | `var == value` |
| Greater Than or Equal To: `>=` | `var >= value` |
| Less Than or Equal To: `<=` | `var <= value` |

One equal sign is the assignment operator `=`, and two equal sign is the equal to (comparison) operator `==`.

You can check multiple conditions with the `if else` statement. Another way to write it is with `elif`.

The final `else` statement is a last resort or considered the "default option" for the decision structure. If the previous coditions are false then we are directed here.

Boolean data type variables can be used in place of condition expressions since the if statement would alread yevaluate to `True` or `False`.

# Logical Operators
A logical operator evaluates multiple conditions (like the comparision operators) with boolean logic (`True` or `False`)
There are three different logical operators [@BroCodez](https://www.youtube.com/watch?v=ix9cRaBkVe0) will discuss:
1. `or`: ONE of the conditions must be `True`
2. `and`: BOTH of the conditions must be `True`
3. `not`: Inverts the conditions (NOT `False` or NOT `True`)

# Conditional Expression
A conditional expression is a one-line shortcut for the if-else statement, which is like a ternary operator in other programming langauges.
It prints or assigns one of two values based on a condition, i.e, X `if` condition `else` return Y.

# String Methods
A string is a series of characters with each being saved in memory by their position or index. When working with indexes we always begin with 0.

There are a list of methods (functions) available to parse strings and return integers:
- `len(var)`: The length function returns an integer of however many characters are within a string
- `var.find("char")`: The find method will return an integer of the first occurance (index) of a given character. If character isn't found, the method will return "-1"
- `var.rfind("char")`: The reverse find (hence rfind) method will return an integer of the last occurance (index) of a given character. If character isn't found, the method will return "-1"
- `var.count("char")`: The count method will return an integer of the number of intstances of a character within the string

There are a list of methods available to parse strings and return strings:
- `var.capitalize()`: The capitalize method will change the first character (in index 0) to an uppercase and return the full string
- `var.upper()`: The upper method will change all characters to uppercase and return the full string
- `var.lower()`: The lower method will change all characters to lowercase and return the full string
- `var.replace("char", "replace")`: The replace method will replace all of a specified character within the string by another given character. It can also be replaced with an empty string `""`

There are a list of methods available to parse string and return booleans:
- `var.isdigit()`: The is digit method will return a boolean of `True` if the string only contains digits (0-9), or `False` if otherwise. 
- `var.isalpha()`: The is digit method will return a boolean of `True` if the string only contains alphabetical characters (a-z or A-Z), or `False` if otherwise. It will print `False` with a space.

To get a list of all string method available top you, use the help function with the string datatype: `print(help(str))`

# String Indexing (Slicing)
Accessing elements of a string, or sequence, using [start : end : step] (indexing operator) one-by-one.
Indexes start at `0` and ends with `len(sequence) -1` because it aligns with how computers manage memory

There is up to three fields you can refer to with with the indexing operator:
1. Start: The starting index is inclusive and assumes if you don't use any colon you're referring to the starting position (0)
2. End: The end index is exclusive and will not include the index you're referring to in the substring
3. Step: The step index is optional and determines the increment between each index for slicing by a given value

To print a range you can do a variety of things:
- `string[:num]`: Use a colon and the end index (you can omit 0 since the start index will assume that as the starting point) to parse the entire string
- `string[num:num]`: Use the start index, a colon, and the end index (will not include the index you're referencing) to parse a range
- `string[num:]`: Use the start index and a colon (will include the index you are referencing) to parse til the end of the string
- `string[::num]`: Use two colons and the step index to parse characters in increments of the given value til the end of the string

Any indexing position can be referenced in reverse, but be sure to remember that the negative inital starting point starts at -1 and not 0.
To rverse a string, set the step index to be negative: `string[::-1]`.

# Format Specifiers
Format specifiers {value:flags} are flags that format a value based on what flags are inserted.
We are able to mix and match flags to better readability.
The syntax for formmatting specifiers are: `{var: [fill][align][sign][#][0][width][,][precision][type]}`

The following is a list of common formatting specifiers for numbers:
- `:.(num)f`: Rounds to that many decimal places (fixed point)
- `:(num)`: Allocates that many spaces as a buffer
- `:0(num)`: Allocates and zero-pads that many spaces (can also insert other characters)
- `:<(num)`: Left justifies using the left angle bracket
- `:>(num)`: Right justifies using the right angle bracket
- `:^(num)`: Center aligns using the caret character
- `:+`: Indicates a positive value using the plus sign
- `: `: Indicates a positive value using a space
- `:-`: Indicates a negative value using the minus sign
- `:,`: Inserts a comma between numbers

# While Loops
While loops `while condition:` are a basic form of decision making that uses the if-else statement logic.
The only difference being that is that while loops repeat (iterate) code based on their conditions.
An `if` statement will execute once and continues to the rest of the program.
While loops use Boolean logic gates - `while` a condition is `True` we iterate something, `else if` the condition is `False`, we exit the loop and continue to the rest of the program.

The syntax for a `while` loop is similar to an `if` statement in that you have the optional else statement.
Like with if staements, you can also include parentheses for readability `while (condition):`.
You can also introduce logical and ternary operators within the condition.

When using while loops be sure to include a way to escape the loop unless you'd get stuck in an infinite loop.

# For Loops
For loops are a basic form of decision making; `while` a condition is `True` we iterate a block of code `for` a given number of times, `else if` it's `False`, we exit the loop.
You can iterate over a range, string, sequence, etc. Syntax for the `for` clause is `for counter in range(start, end, step)`

The `start` parameter is inclusive and beings at index 0.
The `end` paramater is exclsuive, so add one when wanting to include a value within the specified range.
The `step` parameter is optional and also beings at index 0 (unless specified otherwise).

The code block indented after the `for` clause will iterate over the range and will print on newlines unless specified otherwise.
The following print function (not indented) after the block of code is considered outside of the `for` loop so it prints once.-

Because the `for` loop is capable of indexing we can use it to splice strings the same way we would with string indexing by using the `step` parameter.
To count (interate) backwards use the reversed function around the range function `reversed(range(start, end, step))`.
	
The following keywords are also available for the `while` loop:
- The `continue` keyword stays within the same decision logic (i.e., if-else statement)
- The `break` keyword leaves the decision logic

# Nested Loops

Nested loops are loops within another loop (outer and inner). The nested loop syntax is the same regardless of what kindof decision structures are used (e.g., for in while, while in for, etc.).
The outer loop is the loop on the outer most part of the decision structure.
The inner loop is always indented as it's considered part of the code block of the outer loop. The inner loop is always on the inner most part of the decision structure.

Going back to for loops, remember that each print statement ends with a new line escape character (\n) implicitly. This makes `print(x)` the same as `print(x, end="\n")`.
To print everything within the print function on the same line, use the end-line specifier `end="val"`.
The end-line specificer value can be an empty string `end=""`, a space `end=" "`, or any alphanumeric character `end="-"`. 

To iterate a loop, you have to "nest" the loop you want to iterate (repeat) within the code block of another loop by indenting it.
When creating the inner loop, you have to use a different name for the counter variable than from the outer loop.

Note that the outer loop iterates its code block (i.e., the inner loop) x number of times. And the inner loop iterates it's code block y number of times. You can calculate how many executions are made by multiplying the outer loop counter by the inner loop counter (x * y).

You can continue to work within the outer loop by outdenting from the inner loop and it will still be considered within the same code block.

While inside of the nested loop, note that the inner loops iterates as many times as the counter of the outer loop.

To print each iteration of an inner loop on a separate line write a blank print statement `print()`

To write code outside of the nested loop, outdent again until  the next line is in line with the beginning of the outer loop.

# Lists, Sets, & Tuples
Variable are only able to store one value to memory. But with lists, sets, and tuples, they are considered collections, which are single "variables" used to store multiple related values via indices like with strings.

A common naming convention for collections is to make the variable name plural since they are referencing (storing) multiples of related values called elements.

To access elements within the collection, you have to refer to thier index position like with string splicing. The starting index begins at 0. If you try to reference an index that is out of range, then you will get an error message called `IndexError`.

The `in` operator allows you to parse a collection for a specific value and returns a boolean (either `True` or `False`) if it matches user input.

To list the different methods available to your specific collection, use a print statement w/the directory function `print(dir(var))`. This will print the list of available attributes and methods in alphabetical order. To get an in-depth description of each item listed, use a print statement w/the help function `print(help(var))`.

You are able to iterate over collections via loops. Another naming convention dictates that you use a singluar version of the plural used to name your collection, (ex. `for fruits in fruits:`), for the counter variable to help with readability.

There are 4 general purpose collections, but @BroCodez discusses 3 within this chapter:
1. var[]: Lists use brackets and are ordered and changeable. Duplicates OK
2. var{}: Sets use curly braces and are unordered and immutable. Add/Remove OK. NO duplicates
3. var(): Tuples use parentheses and are ordered and unchangeable. Duplicates OK. FASTER

## Lists
Lists surround thier values with a square bracket and separate each with a comma `var[val1, ...]`.

Like w/a string, you can splice your list by setting a start index, end index, and step index to print a range of elements. Because lists are ordered and changeable, we can change the value of specific indices by using the assignment operator.

There are a few specific methods are available for lists `var[]`:
- `len(list)`: The length method prints the number of indices within a collection
- `.count(value)`: The count method prints the number of instances of a given value within a list. This is possible since duplicates are able to exist within lists. If no element is found with that specific value, then it will print "0"
- `.append(list)`: The append method adds elements to the end of the list
- `.remove(list)`: The remove method removes elements from the given index within the list
- `.insert(pos,value)`: The insert method adds elements to any index within the list
- `.sort(list)`: The sort method will sort the elements within a list in ascending (A-Z) alphabetical order
- `.reverse(list)`: The reverse method directly after the sort method will sort elements within a list in descending (Z-A) alphabetical order. Otherwise, the reverse method on its own will sort a list in descending numerical order based on thier indices
- `.index(value)`: The index method will returm the numerical index position of an element matching the user input. If there isn't a matching value, you will get an error message called `ValueError`
- `.clear()`: The clear method will delete all elements within the list

## Sets
Sets surround thier values with a curly brace and separate each with a comma `var{val1, ...}`.

Since sets are unordered, whenever the set is printed to console the elements in the set will contain the same values, but will be stored in different positions, making it random. This makes it so sets are not capable of having duplicate values and we aren't able to reference elements within a set via indices. If we try anyways, we will get an error message called `TypeError`.

To "parse" a set for potential values, we can use the `in` operator to check for values within a set `print(val in set)`, this will return a boolean value of `True` or `False`.

Because sets are unordered, it also makes them immutable, meaning we cannot directly change a set element value. We can, however, add and remove elements within a set via methods:
- `.add(value)`: The add method allows us to append values to the set
- `.remove(value)`: The remove method allows us to delete values from the set
- `.pop()`: The pop method will delete whichever element is first, which is random because of the nature of a set
- `.clear()`: The clear method will delete all elements within the set

Sets work best for when you are working with constants.

## Tuples
Tuples surround thier values with parentheses and separate each with a comma `var(val1, ...)`.

Becuase tuples are ordered and unchangeable, they are FASTER than lists because data are in fixed positions.
- `.index(value)`: The index method will return the numerical index positon of an element
- `.count(value)`: The count method will return the number of instances of a given value within the tuple

Tuples work best with fixed lists.

# 2D Collections
2D collections (or arrays) are two-dimentional collections that are made up of collections.
You can create a 2D array works with any kind of collection (ex. a list[] made of lists). These are useful when working with matrices or grids of data, similar to an excel spreadsheet.

2D arrays follow the same naming convensions for 1D arrays (lists, tuples, sets, etc.), in that the name of the outer array is more broad than the inner arrays (ex. groceries are made of fruits, vegatables, and meats).

To create a 2D array, think of nested loops, where you would create a 1D collection first, then "nest" the other 1D collections within the elements of ther "outer" collection.

Think back to how you would reference elements within a 1D array:
- Use the `print()` function to print the elements within a 1D array
- Reference the index position of an element to print a specific element from within the array, starting from 0
- Use the assignment operator (`=`) w/the index of the element you would like to change

The same logic applies when parsing through 2D arrays.
If you used the `print()` function and referenced an element within a 2D array, it would print every 1D array separated by commas within a square bracket on one line.

To access specific elements within a 2D array, remember it can be parsed similarly to that of a grid, w/1D array variable names acting as rows and the elements within them acting as columns.
Like a 1D list to reference a element (which is an entire list), use the index starting from 0. To access an element found within one of the rows (list), you need to reference that specific index too.
You can think of this system like coordinates on a grid.

Like with 1D lists, if you try to access an indices out of range, you will get the 'IndexError'.

To print entire lists from within a 2D list, use loops.
To iterate over the elements within lists of a 2D list, use nested loops.

You can mix and match different types of collections within 2D lists.

It isn't necessary to give the elements within a 2D names, but it is great for readability.

# Dictionaries
A collection (array) of `{key:value}` pairs which are ordered (via indicies) and chanageable. NO duplicates are allowed.
A dictionary is one of the four basic types of collections for jr. devs.
To initialize a dictionary enclose the elements (`{key:value}` pairs) within with a set of curly braces, like a set{} array, and separate with commas (`,`).

Like with other 1D arrays, you can see all of the possible attributes and methods for the dictionary{} using a print statement w/the directory method `print(dir(dic_name))`. To get an in-depeth description of each attribute and method use a print statment w/the help method `print(help(dic_name))`.

The following are a few methods available to the `dic{}` array:
- `.get({key})`: The get method parses a dictionary for a given value. If no values are found, the method will return `None`, which can be used in deicsion structures, like if-statements, like Booleans as an off-state (or `False`)
- `.update({key}:{value})`: The update method can add values to our dictionary using the same syntax for initializing the dictionary. It can also be used to update preexisting values
- `.pop("{key}")`: The pop method can remove specific values from the dictionary via a key (like an index/element)
- `.popitem()`: The pop item method can remove the latest key value that was inserted
- `.clear()`: The clear method will truncate all keys from the dictionary
- `.keys()`: The keys method will return an object that resembles a 1D list of all of the keys (i.e., indices) from a given dictionary array
- `.values()`: The values method will return an object that resembles a 1D list of all of the values (i.e., elements) from a given dictionary array
- `.items()`: The items method will return an object that resembles a 2D list of all of the `{key:value}` pairs from a given dictionary array

# Random Numbers
To generate random numbers import the random library module `import random` at the top of the file.

For a list of all of the methods use the print statement w/the help method `print(help(random))`.

Random number generators are great for games, liek D&D dice, card, rock papper scissors, etc.

The following is a list of methods availble to the random library
- `.randint(start, end)`: The random integer method prints integers within a range that is inclusive. You can also use integer variables within the range
- `.random()`: The random float method prints floating-point number within a range of 0 and 1 that is inclusive. You can use the decimal format specifier to limit the number of decimal places
- `.choice(seq)`: The choice method prints a random elemnt from a list or a sequence (best w/tuples)
- `.shuffle(seq)`: The shuffle method reorders the elements within a sequence (best w/lists)

# Functions
Instead of re-writing code multiple times, we can utilize functions to reference entire code blocks as reusable code. To initialize a function, use the keyword `def` (for definition) and the function name followed by parentheses `def funct()`.

To call (or invoke) the function just type out the function name w/parentheses `funct()`

You can send data into a function as arguments within the paraentheses `funct(args)`. When sending data, be sure to have a matching set of parameters being referenced within the code block

The `return` statement is used at the end of a function and sends a result back to the caller. You can either send a variable or an operation, and it will send back the result all the same.
Ex. `z = funct(x, y)` is like using the assignment operator for z = result of function.

# Arguments
@BroCodez goes over four types of arguments, but has covered two so far:
1. Positional arguments are used when initializing functions
2. Default arguments are used for flexiblity and legibility
3. Keyword arguments
4. Arbitrary arguments

## Positional Arguments
A positonal argument is the value passed through a parameter by thier position in the arg. tuple `function(arg1, etc.)`

## Default Arguments
A default argument is a default value assignend to a parameter. The default arg. is used when the arg. is omitted and makes for a more flexible and legible function call.
These are best used for arguments with consistent/known base values.

When calling a function you can set default parameters by initializing them in the function definition.
`function(arg1 = val, etc.)`

You don't have to pass values for default arg., making the code cleaner.

## Keyword Arguments
A keyword argument is an arg. preceded by an identifier to help w/readability.
They are used for clarification so args. always appear in the order you intend for them to be.

Order of keyword arguments doesn't matter; Be sure to put position arg. first
Else you get "SyntaxError: Postional argument follows keyword argument"

`end` is a keyword argument for the bulit-in print() statement `print(var, end=" ")` and will print vairables on the same line.

`sep` (short for separate) is a keyword arg. for the print() statement `print(var, sep=" ")`  which outputs character(s) between strings on the same line.

## Arbitrary Arguments
Arbitrary refers to having to pass a varying amount of arguments, or when you aren't sure of how many will be passed through a function when invoked. Without arbitrary args. you would only be able to pass a set amount of args. defined previously in the function definition.

Arbitrary args. are prefixed w/the unpacking operator (`*`).

There are two kinds of arbitrary args.:
1. `*args`: Non-key args. allow you to pass multiple non-key arguments into a tuple()
2. `**kargs`: Keyword args. allow you to pass multiple keyword-arguments into a dictionary{}

The `type()` method will return the data type of the name of the function passed into it.
For non-key args., it will return `<class 'tuple'>`, and for keyword-args., it will return `<class 'dict'>`.

# Iterables
An iterable is an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

The iterable in most loops is called the counter variable. It should be named according to what's being counted for readability.

The following are considered iterables:
- `Lists[]`: You can iterate them in order or in reverse w/the `reversed()` method
- `Strings[]`: These are a special type of list array, so you can iterate them in order or in reverse w/the `reversed()` method
- `Tuples()`: You can iterate them in order or in reverse w/the `reversed()` method
- `Sets{}`: You can only iterate them in order, otherwise you will get the `TypeError` message "'set' object is not reversable"
- `Dictionaries{}`: You can iterate them in order and either print only the `{keys}`, the `{values}`, or the `{key}:{value}` pair

# Membership Operators
Membership operators are used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)

The following are considered membership operators:
- `in`: The `in` keyword will return a boolean value of `True` or `False`
- `not in`: # Using the `not` keyword would reverse the resting state

# List Comprehensions
List comprehensions are a concise way to create lists in Python. They are more compact and easier to read than traditional loops.

The syntax for a comprehensive list is as follows: `[(expression) for value in iterable if (condition)]`.

# Switch (Mathc-case) Statements
A match-case, or `switch`, statement is an alternative to using many `elif` statements that was added to Python in v.3.10. `switch` statements are often used because the code is cleaner and the syntax is more readable.

`switch` statements are similar to `if` statements, as code blocks are executed if a value matches a `case` or a condition. The default (or `else`) statement is the underscore, which is a wildcard `case _:`

# Modules
Modules are python files (built-in or custom-made) containing code you want to include in your program by using the `import` keyword. Modules are useful to break up a large program into reusable separate files.

For a list of all of the modules within the standard python library use the help() method and pass in the word "modules" `print(help("modules"))`

You are able to give imported modules custom names, or aliases, with the `as` keyword:  `import math as m`. Whenever using methods from within the module, you would refer to it by its alias.

Instead of importing the entire module, you can also specify which methods you would like to access with the `from` keyword. This method isn't used as much because of possible of variable naming conflictions.

You can import custom-made modules via referencing their file names so long as they are within the same project folder. File names for methods must not contain underscores or start with numbers.

# Scope Resolution
Variable scope refers to where a variable is visible and accessible. Scope resolution is structured as follows: (LEGB Rule) Local -> Enclosed -> Global -> Built-in

Functions are not capable of seeing inside of other functions beside themselves. Thus, we cannot cross-reference variables from between function unless we pass them within the function. Becuase of this you can have multiple of the same variable name within different functions.

You can declare functions within the same scope (i.e., enclosed functions). If there was no local variable declaration within the function, it would use the enclosed scope variable instead.

The global scope refers to variables located outside of any functions. If there are no local versions, and no enclosed versions, then the function will refer to the global variable.

# Main Method
The main method allows for functions and classes within the main() module to be reused without the main block of code executing. Other scripts that have been imported into the main method can also be run standalone. You can check the name of a script with the following line of code: `if __name__ == "__main__"`.

You can also use the `print(dir())` to get a list of all available methods and files that can be imported. To import everything from a file use the asterisk (`*`) since it means all. 

The program starts by checkign the filenames of all scripts that have been imported to see if it is `__main__`. Then the program implicity starts at the main method from which you can call other methods.

