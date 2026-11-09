# Setup C++ File
C++ is used because it is a fast langauge and is commonly used in advanced graphics applications, embedded system, and video games.
It is considered a middle-level programming langauge: For context, Python, Java, and C# are considered high-level languages, or are closer to human language.

There are two things you need to download to get started coding in C++:
1. A Text Editor or an Integrated Development Environment (IDE)
- You can use VSCodium, CodeBlocks, Notepad, etc. You can Go to [JetBrains.com](https://www.jetbrains.com/clion/) and download the latest version of the CLion IDE community version (it's free :3)
2. A C/C++ Compiler
- Go to [isocpp.org](https://isocpp.org/get-started) and download the latest version of [Clang](https://clangd.llvm.org/installation.html) or [GCC](https://gcc.gnu.org/install/). If you are using Windows, you can also download [MinGW](https://sourceforge.net/projects/mingw/).

## Comments
Remember when setting up a C++ program to document what your program does as you develop a project.
It is good practice as when you eventually return to said program or for other developers to be able to understand what you are doing.

Comments aren't executed as code by the compiler and are used as notes for either yourself or other developers. There are a few types of comments:
- A multiline (block) comment begins with a slash and an asterisk `/*` and can span multiple lines
- A single line comment begins with two slashes `//` and spans a single line

C++ doesn't have docstrings like higher level programming languages. Instead you can use a common format of documentation within block comments, or with a triple-slash `///` syntax, called Doxygen.
- The `@brief` tag to provide a brief description of the function or class
- The `@param` tag to describe the parameters of the function
- The `@return` tag to describe the return value of the function

## First Program
When creating a C++ file, first we have to include the header file to import functions for us to be able to execute code.
The `#include <iostream>` line contains basic functions for input/output operations that allows us to write output, read input, and write a newline.

This isn't talked about in this section, but a `namespace` is a named scope that groups related names and helps prevent naming conflicts.
The C++ standard library `std` puts many of its names, including `cout`, `cin`, `string`, etc. inside the `std` namespace.
To use names within the `std` namespace without having to write `std::` each time utilize the `using` keyword: `using namespace std;`.

Every statement in C++ ends with a semicolon `;`. This is how the compiler knows that the statement is complete and can be executed. If you forget to include a semicolon, the compiler will throw an error.

When writing output to the console, we use the standard output stream `std::cout` and the left-shift operator `<<`.

The next line of code will print a string on the same line as the previous output.
This is because there is no newline character `\n` or `std::endl` manipulator at the end of the previous statement.

The end of line `std::endl` manipulator is used to insert a newline escape character `\n` and flush the output buffer.
This is useful when you want to ensure that all output is displayed immediately, especially in cases where the program may be waiting for user input or performing other tasks.

You can also use the backslash `\` to escape special characters in a string. In this case, it is used to escape the newline character `\n` so that it is treated as a literal character in the string.
You can also directly use the newline escape character `\n` after the left-shift operator to insert a new line in the output. It is similar to `std::endl`, but it does not flush the output buffer.

When ending a C++ funciton, we use the `return` keyword to end the current function and, if specified, send a value back to whoever called it.
In the `main()` funciton, `return 0;` ends the program and reports successful completion to the operating system. If the function returns a non-zero value, then there was an issue. 

## Example
```cpp title="01_setup.cpp"
// Header Files
#include <iostream>
//using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    std::cout << "Hello, world. ";
    std::cout << "It is really sunny today!" << std::endl ;
    std::cout << "I would like to go to the park." << "\n";
    std::cout << "Then, I think I'd like to go for icecream.\n";
    std::cout << "I would like two scoops of vanilla!";

    return 0;
}
```

# Variables and Basic Data Types
In C++, variables are use to store and manipulate data during the execution of a program.
A variable is a named storage location in memory that can hold a value of a specific data type.

There are two steps to creating a variable in C++:
1. Declare the variable's data type and name (identifier)
2. Initialize the variable with a value (optional, but recommended)

The data type of a variable determines the kind of data it can hold.

## Primitaive Data Types
There are different primitaive data types in C++ that you can use to store data. Some common types include:
- `int` is used to store whole numbers (e.g., 1, -5, 100)
- `float`: Used to store decimal numbers (e.g., 3.14, -0.5, 2.718)
- `double`: Used to store double-precision decimal numbers (e.g., 3.14159, -0.0001, 2.71828)
- `bool`: Used to store boolean values (`true` or `false`)
- `char`: Used to store single characters (e.g., 'a', 'Z', '1', '$')

### `int`
To store a whole number, you use the `int` data type, which is used to represent integer value or whole numbers without any decimal points.

When assigning a data type to a variable name, you are declaring the variable: `int age;`.
When assigning a value to a variable, you are initializing the variable: `age = 23;`.

You are able, and encoruaged, to declare and initialize a variable in a single line of code: `int year = 2003;`.

You are able to initialize integers with decimal portions, but it will be truncated and the value output to console will be the whole number.

Also, when outputting variables to the console, pay attention to the left-shift `<<` operator, which is used to concatenate (combine) multiple values and strings together for output, and include a space in the string to show between the text and the value.

### `float` and `double`
`float` and `double` store approximate real-number values - numbers that may have a fractional part, or very large or small numbers.
They store these values in binary-floating point form (using a sign, significand, and exponent), not as exact decimal text.
Some decimal values, therefore, cannot be represented exactly.

To store a floating-point number, you use the `float` data type, which is used to store decimal numbers within 6-7 places as it uses 32 bits.
To store a double-precision decimal number, you use the `double` data type, which is used to store decimal numbers within 15-16 places as it uses 64 bits.

When declaring a `float`, include an `f` character a in the value when declaring to mark the first literal as a `float`, otherwise the literal would be considered `double` by default.

In C++, it's a general rule that `double` is guaranteed to provide at least as much precision as `float`.

### `bool`
The `bool` data type is used to store boolean values, which can be either `true` or `false`.
When printing a boolean variable, `false` is represented as 0, and `true` is represented as 1.

### `char`
The `char` data type is used to store single characters, which includes letters (a-z, A-Z), digits (0-9), and special characters ($, #, @, etc.).
It can be overloaded, though it isn't recommended, and will store multiple characters, but it will only print the last character to the console.

## `string` Object Class
The `<string>` header file is included to use the `std::string` class, which allows you to work with strings in C++: `#include <string>`.

`string` is not a primitive data type; it is an object class that is used to store a sequence of characters `char` (text).
The `string` object is part of the C++ Standard Library, and it provides various functions and methods to manipulate strings.

The `string` objects are declared the same way as the primitive data types, and can also be initialized in a single line of code.
You can also initialize a `string` object with spaces in the value.

## Example
```cpp title="02_variable.cpp"
// Header Files
#include <iostream>
#include <string>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int age = 23;
    float pi = 3.14159;
    double gpa = 3.53;
    bool isStudent = true;
    char grade = 'A';
    string name = "8BitSoftware";

    cout << "Hello, my name is " << name << "." << endl;
    cout << "I am " << age << " years old." << endl;
    cout << "Am I a student? " << isAmerican << endl;
    cout << "My grade in class is " << grade << "." << endl;
    cout << "My gpa is " << gpa << "." << endl;
    cout << "My favorite number is " << pi << "." << endl;

    return 0;
}
```

# `const` Keyword
The `const` keyword in C++ is used to declare variables whose values cannot be changed after initialization because they are constant.
This means that once a `const` variable is assigned a value, it cannot be modified throughout the program (variable is then considered read-only).
Using `const` can help prevent accidental changes to variables that should remain constant, improving code safety and readability.

A popular naming convention for `const` variables is to use all uppercase letters with underscores to separate words.

## Example
```cpp title="03_const.cpp"
// Standard-library includes
# include <iostream>
# include <string>

using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    const double PI = 3.14159;
    double radius = 5.0;

    double circumference = 2 * PI * radius;

    cout << "The circumference of a circle with radius " << radius << " is: " << circumference << endl;

    return 0;
}
```

# Namespaces
The `namespace` keyword in C++ is used to group related variables, functions, and classes under a single name to avoid naming conflicts in larger programs.
Namespaces help organize code and prevent collisions between identifiers that may have the same name but are used in different contexts.

The `using` keyword allows you to use names from a namespace without having to prefix them with the namespace name.
Ex. `using namespace std;` allows you to use `cout` and `endl` without the `std::` prefix.

You can declare a namespace as you would a function: with the `namespace` keyword followed by the namespace name and curcle braces `{}`.
Within the namespace, you are able to declare similarly named variables, functions, and classes from the global scope within the namespace.

Any variable declared within the `main()` function is cosidered within the global namespace, which means it is accessible throughout the entire program unless shadowed by a local variable with the same name.
To access a variable, function, or class within a namespace, you can use the scope resolution operator `::` followed by the namespace name and the identifier name.

## Example
```cpp title="04_namespaces.cpp"
# include <iostream>
using namespace std; 

namespace alt { int x = 1; }

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int x = 0;

    cout << "Global namespace x is: " << x << endl;
    cout << "\"alt\" namespace is: " << alt::x << endl;

    return 0;
}
```

# `typedef`and Type Aliases
In C++, the `typedef` keyword is used to create an additional name (alias) for an existing data type, allowing you to define a new name for a type that can be used interchangeably with the original type.
This can be useful for improving code readability, simplifying complex type declarations, or creating more meaningful names for types in your program.

A common naming convention for `typedef` aliases is to use a descriptive name that ends with `_t`, indicating that it is a type alias.
You can also create a `typedef` alias for a simple data type like `string`, which can make the code more readable and easier to understand.

`typedef` has been largely replaced by the `using` keyword in modern C++ (C++11 and later), which works better with templates. However, `typedef` is still widely used and supported in C++.
The `using` keyword is a more modern way to create type aliases in C++. It provides better support for templates and is generally considered more readable.

## Example
```cpp title="05_typedefaliases.cpp"
#include <iostream>
using namespace std;

// typedef string text_t;
// typedef int number_t;

using text_t = string;
using number_t = int;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    text_t myText = "Hello, World!";
    number_t age = 23;

    cout << "My text is: " << myText << endl;
    cout << "My age is: " << age << endl;

    return 0;
}
```

# Artithmetic Operators
Arithmetic operators in C++ are used to perform mathematical operations on numeric values. The basic arithmetic operators include:
- Addition (`+`): Adds two operands together
- Subtraction (`-`): Subtracts the right operand from the left operand
- Multiplication (`*`): Multiplies two operands together
- Division (`/`): Divides the left operand by the right operand
- Modulus (`%`): Returns the remainder of the division of the left operand by the right operand (only applicable to integer types)

The modulus operator can be useful in various scenarios, such as determining if a number is even or odd by checking if the remainder is 0 (even) or 1 (odd).

These operators can be used with variables, constants, and expressions to perform calculations in C++

You can use arithmetic operators to perform calculations in two ways:
1. Using the arithmetic operator directly in an expression: `numStudents + 5;`
2. Using the arithmetic operator in an assignment statement: `numStudents = numStudents + 5;`

With the assignment statement, you are updating the value of `numStudents` by adding 5 to its current value and assigning the result back to `numStudents`.
You can used the shorthand compound assignment operator `+=` to achieve the same result in a more concise way: `numStudents += 5;`

The increment `++`/decrement `--` operators are shorthand ways to increase or decrease the value of a variable by 1.
This operator can be used in two forms: prefix (`++numStudents`) and postfix (`numStudents++`).

All arithmetic operators have an order of precedence, which determines the order in which operations are performed in an expression.
The order of precedence for arithmetic operators is as follows (PEMDAS):
1. Parentheses `()`
2. Multiplication `*`, Division `/`, and Modulus `%` (from left to right)
3. Addition `+` and Subtraction `-`
4. Assignment `=`, Compound Assignment `+=`, `-=`, `*=`, `/=`, `%=` (from right to left)
5. Increment `++` and Decrement `--` (from right to left)
6. Negative `-` (unary minus) and Positive `+` (unary plus) (from right to left)

You can use parentheses `()` to group operations and override the default order of precedence.
Operations within parentheses are performed first, followed by multiplication, division, and modulus, and finally addition and subtraction.

## Example
```cpp title="06_arithmetciops.cpp"
#include <iostream>
using namespace std;

using numbers_t = int;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue
    numbers_t value = 4
    numbers_t result = (5 - (value + 5) * 3 / 4) % 2

    cout << " The result is: " << result;

    return 0;
}
```

# Type Conversion
Type conversion changes a value from one data type to another. C++ conversions can happen implicitly, when the compiler performs a permitted conversion automatically, or explicitly, when the code requests a conversion.

An implicit conversion can happen when assigning a value to a variable of another type. For example, assigning a `double` to an `int` discards the fractional part by truncating toward zero; it does not round the value. Converting an `int` to a `double` keeps the integer value and represents it with a floating-point type.

Use `static_cast<new_type>(value)` to make an explicit conversion. This is the preferred C++ style over a C-style cast such as `(int)value`, because it makes the conversion easier to recognize and review. Converting a floating-point value to an integer this way also truncates toward zero.

`char` is an integer type that is commonly used to store character values. Assigning an integer to a `char` converts that integer to the corresponding character value in the implementation's character encoding; this is not guaranteed to be ASCII. When a `char` is printed, the stream displays it as a character. Cast it to `int` to display its numeric value.

## Example
```cpp title="06_arithmetciops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    double original = 3.14;
    int implicitInt = original;
    double implicitDouble = 3;
    int explicitInt = static_cast<int>(original);
    double convertedBack = static_cast<double>(explicitInt);

    cout << "Implicit double-to-int: " << implicitInt << endl;
    cout << "Implicit int-to-double: " << implicitDouble << endl;
    cout << "Explicit double-to-int: " << explicitInt << endl;
    cout << "Converted back to double: " << convertedBack << endl;

    char letter = static_cast<char>(100);
    cout << "Character value: " << letter << endl;
    cout << "Numeric value of character: " << static_cast<int>(letter) << endl;
    cout << "Character for numeric value 101: " << static_cast<char>(101) << endl;

    return 0;
}
```

# User Input

## Example
```cpp title="06_arithmetciops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Math Functions

# `if` statements

# Switches

# Ternary Operator

# Logical Operators

# `String` Methods

# `while` Loops

# `for` Loops

# `break` and `continue`

# Nested Loops

# `random`

# User Defined Functions

# `return` Keyword

# Overloaded Functions

# Variable Scope

# Arrays

# `sizeof()` Operator

# Iteration

# `foreach` Loop

# Pass Array to a Function

# Search array for an element

# Sort an array

# `fill()` Function

# Fill an array with User Input

# Multidimentional Arrays

# Memory addresses

# Pass by `value` vs. pass by `ref`

# `const` Parameters

# Pointes

# `null` pointers

# Dynamic Memory

# Recursion

# Function Templates

# `structs`

# Pass `structs` as arguments

# `enum`

# Object Oriented Programming

# Constructors

# Constructor Overloading

# Getters and Setters

# Inheritance
