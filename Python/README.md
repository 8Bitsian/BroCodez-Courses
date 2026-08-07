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