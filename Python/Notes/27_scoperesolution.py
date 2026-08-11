# Scope Resolution

# Variable scope is where a variable is visible and accessible
# Scope resolution is structured as follows: (LEGB) Local -> Enclosed -> Global -> Built-in

# Functions are not capable of seeing inside of other functions beside themselves, which is why we pass variables onto functions
def function_1():
    # `a` declared locally within function_1()
    a = 1
    # You cannot print variable b since it's in function_2()
    print(a)    # Print "1"

def function_2():
    # `b` declared locally within function_2()
    b = 2
    # You cannot print variable a since it's in function_1()
    print(b)    # Print "2"

function_1()
function_2()

# You can have multiple of the same variable name within different functions
def function_3():
    x = 3
    print(x)    # Print "3"

def function_4():
    x = 4
    print(x)    # Print "4"

function_3()
function_4()

# You can declare functions within the same scope (i.e., enclosed functions)
def function_5():
    x = 5
    print(x)    # Prints "5"
    def function_6():
        # If there was no local variable declaration within the function, it would use the enclosed scope variable instead
        print(x)    # Print "5"
    function_6()
function_5()

# The global scope refers to variables located outside of any functions
x = 7
def function_7():
    # There is no local version, and no enclosed version, then the function will refer to the global variable
    print(x)    # Print "7"

function_7()

from math import e
# If there is a global version declared for Euler's number, then it would overtake the imported math constant
# e = 3
def function_e():
    print(e)    # Prints "2.718281828459045"
function_e()