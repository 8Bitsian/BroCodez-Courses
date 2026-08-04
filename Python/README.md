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
