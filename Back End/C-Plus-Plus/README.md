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
```cpp title="07_typeconversion.cpp"
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
We can accept user input in C++ by manipulating the standard input/output streams using insertion operators:
- The `cin` object is used to read input from the input stream (keyboard) is paired with the extraction operator (`>>`) to extract data from the input stream and store it in variables
- The `cout` object is used to write output to the output stream (console) is paired with the insertion operator (`<<`) to insert data into the output stream for display

## Example
```cpp title="08_userinput.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    cout << "Enter your age: ";
    cin >> age;
    cout << "Enter your full name: ";
    getline(cin >> ws, name);

    cout << "Hello, " << name << "!" << endl;
    cout << "You are " << age << " years old." << endl;

    return 0;
}
```

# Math Functions
Math related functions in C++ are part of the `<cmath>` library, which provides a variety of mathematical operations and constants.
These functions can be used for tasks such as calculating square roots, trigonometric functions, logarithms, and more.

If you head to www.cplusplus.com/references/cmath/ you can find a comprehensive list of all the functions available in the `<cmath>` library, along with their descriptions and usage examples.

The `max()` and `min()` functions are standard functions in C++ that return the maximum and minimum of two values, respectively.
They are part of the `<algorithm>` header, but can also be used with `<cmath>` for basic types.

The following functions are part of the `<cmath>` library and provide various mathematical operations:
- The `sqrt()` function returns the square root of a value
- The `pow()` function raises a value to the power of another value
- The `abs()` function returns the absolute value of a number
- The `round()` function rounds a floating-point number to the nearest integer
- The `ceil()` function rounds a floating-point number up to the nearest integer
- The `floor()` function rounds a floating-point number down to the nearest integer

## Example
```cpp title="09_mathfunctions.cpp"
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    double x = 3.5;
    double y = 4.0;
    double z;

    z = max(x, y);
    cout << "The maximum of " << x << " and " << y << " is " << z << endl;
    z = min(x, y);
    cout << "The minimum of " << x << " and " << y << " is " << z << endl;

    z = sqrt(x);
    cout << "The square root of " << x << " is " << z << endl;
    z = pow(x, y);
    cout << x << " raised to the power of " << y << " is " << z << endl;
    z = abs(-x);
    cout << "The absolute value of " << -x << " is " << z << endl;

    z = round(x);
    cout << "The rounded value of 3.6 is " << z << endl;
    z = ceil(x);
    cout << "The ceiling value of 3.2 is " << z << endl;
    z = floor(x);
    cout << "The floor value of 3.8 is " << z << endl;

    return 0;
}
```

# `if` statements
C++ has decision structures to decide which statements to execute based on certain conditions.
The `if` statement is used to execute a block of code if a specified condition is true. If the condition is false, the block of code is skipped.

The `if` statement uses conditional operators to compare values within the parentheses `()`.
The condition is evaluated to either true or false. A few condition operators are:
    1. `==` (equal to)
    2. `!=` (not equal to)
    3. `>` (greater than)
    4. `<` (less than)
    5. `>=` (greater than or equal to)
    6. `<=` (less than or equal to)

The `else if` statement is used to specify a new condition to test, if the previous condition was false. If the new condition is true, the block of code inside the `else if` statement will be executed.
The `else` statement is used to execute a block of code if the condition(s) in the `if` and `else if` statements are false. 

## Example
```cpp title="10_ifstatements.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int age
    cout << "Please enter your age: ";
    cin >> age;

    if (age >= 120>) {
        cout << "Entered invalid age." << endl;
    } else if (age >= 21) {
        cout << "You are an adult." << endl;
    } else if (age >= 0) {
        cout << "You are a minor." << endl;
    } else {
        cout << "Entered invalid age." << endl;
    }

    return 0;
}
```

# Switches
In C++, `switch` statements are another decision structure that act as an alternative to multiple `if else` statements.
They are used when you have a variable that can take on multiple discrete values.
The `break` statement is used to exit the switch statement after a case has been executed.

## Example
```cpp title="11_switch-statements.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    char grade;
    cout << "Enter letter grade: ";
    cin >> grade;

    switch (grade) {
        case 'A':
            cout << "You did fantastic!";
            break;
        case 'B':
            cout << "You did great!";
            break;
        case 'C':
            cout << "You did okay.";
            break;
        case 'F':
            cout << "You are failing.";
            break;
        default:
            cout << "Enter a letter grade (A-F)";
    }

    return 0;
}
```

# Ternary Operator
In C++, the ternary operator `?:` is a shorthand way to write an if-else statement.
It has the syntax: `condition ? value_if_true : value_if_false`.

## Example
```cpp title="12_ternary-ops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    bool isRaining = true;

    /*
        // Example of an if-else statement
        if (isRaining) {
            cout << "It is raining." << endl;
        } else {
            cout << "It is sunny." << endl;
        }

        // Example of a ternary operator
        (isRaining) ? cout << "It is raining." << endl : cout << "It is sunny." << endl;
    */

    cout << (isRaining ? "Take an umbrella." : "No need for an umbrella.") << endl;

    return 0;
}
```

# Logical Operators
In C++, logical operators are used to compare multiple conditions. There are three kinds of logical operators:
1. The and operator `&&` checks if two or more conditions are `true`
2. The or operator `||` checks if at least one of two or more conditions are `true`
3. The not operator `!` reverses the logical state of its operand and checks for the inverse of the condition

## Example
```cpp title="13_logicalops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int temperature;
    bool isSunny = true;

    cout << "Enter the temperature (°C): ";
    cin >> temperature;

    if (temperature > 0 && temperature < 30) { 
        cout << "The temperature is nice." << endl;
    } else if (temperature <= 0 || temperature >= 30) {
        cout << "The temperature is bad." << endl;
    } else {
        cout << "Invalid input." << endl;
    }

    if (!isSunny) {
        cout << "It will rain." << endl;
    } else {
        cout << "It is sunny." << endl;
    }

    return 0;
}
```

# `String` Methods
In C++, a string is a sequence of characters that can be manipulated and stored in memory.
The C++ Standard Library provides the `std::string` class, which is part of the `<string>` header, to handle strings more easily than using character arrays (C-style strings).

The following are examples of string methods the standard library includes:
- The `length()` method will return the number of characters within a string
- The `empty()` method will return a boolean value depending on whether there are characters within a string
- The `append()` method will insert a string within the parentheses to the end of another string
- The `at()` method will return the character at the specified index, starting with 0
- The `insert(pos, string)` method will insert a string at a speicied index within the 
- The `find()` method will return the first index of the specified character within a string
- The `erase(start, end)` method will remove a portion of a string at a given index range
- The `clear()` method will remove all characters within a string

## Example
```cpp title="14_stringmethods.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string name;
    cout << "Enter your name: ";
    getline(cin >> ws, name);

    cout << name.length() << endl;

    (name.empty()) ? cout << "The string is empty." << endl : cout << "The string is full." << endl;

    name.append("@gmail.com");
    cout << name << endl;

    cout << name.at(0) << endl;

    name.insert(0, "Your email is: ");
    cout << name << endl;

    cout << name.find(' ') << endl;

    name.erase(0, 15);
    cout << name << endl;

    name.clear();
    (name.empty()) ? cout << "The string is empty." << endl : cout << "The string is full." << endl;

    return 0;
}
```

# Loops
This section is a combination of chapters from @BroCodez that include `while`, `do while`, `for`, and `for each` loops, as well as the `break` and `continue` keywords and nested loops.

## `while` Loops
In C++, `while` loops are similar to `if` staements, in that they check if a condition is `true` or `false`, and differ in that they use that check to determine whether to repeat, or iterate, the statements within the code block between thier curly braces.

`if` `name` is empty then print "The string is empty." `else` print "The string is full."
`(name.empty()) ? cout << "The string is empty." << endl : cout << "The string is full." << endl;`

A `while` loop will repeat until the condition within the parentheses is valid or `true`
A loop with no way out is considered an infinite loop.

The syntax is: `while (condition) { ... }`

### Example
```cpp title="15_while-loops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string name;
    while (name.empty()) {
        cout << "Enter your name: ";
        getline(cin >> ws, name);
    }
    cout << "Hello " << name << endl;

    return 0;
}
```

## `do while` Loops
In C++, a `do-while` loop executes a block of code after `do` and iterates if a condition is valid or `true`
The syntax is: `do { ... } while (condition);`

### Example
```cpp title="16_dowhile-loops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int number, value = 0;
    do {
        cout << "Enter a value: ";
        cin >> number;
        value += number;
    } while (value < 10);
    count << "Sum: " << value << endl;

    return 0;
}
```

## `for` Loops
In C++, a `for` loop executes a block of code a specified amount of times.

Within the condition for the for loop there are three parts we can include:
1. The index which acts as a counter for the amount of times the code block executes
2. The limit which acts as a stopping point for the loop
3. Then the increment/decrement for the counter to add or subtract by the amount of loops

You can set the index to be anything greather than or equal to 0.

When incrementing/decrementing you are able to skip iterations by using values more than 1.

The syntax is: `for (index; limit; increment/decrement ) { ... }`

### Example
```cpp title="17_for-loops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    for (int i = 1; i <= 10; i++>) {
        cout << "Countdown: " << i << endl;
    }
    cout << "Happy New Year!" << endl;

    return 0;
}
```

## `foreach` Loop
In C++, a `for each` loop eases the traversal over an iterable data set, such as an array.

Using a `for` loop, you must include three statements, an index, a condition, and then increment/decrement the index.
The `for` loop allows you to increment/decrement, or skip iterations.

The `for each` loop is simpler than a for loop, but it is less flexible syntax wise.
It only allows us to start at the beginning index and increment forward towards the ending index.

The syntax is: `for (element in dataset) { ... }`
    
### Example
```cpp title="18_foreach-loops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string transformers[] = {"Starscream", "Sunstreaker", "Cosmos"};
    for (string bot : transformers) {
        cout << bot << endl;
    }

    return 0;
}
```

## `break` and `continue`
In C++, the `break` keyword will step out of a loop (also seen in `switch` statements).
The `continue` keyword will skip a current iteration.

### Example
```cpp title="19_break-continue.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    for (int i = 1; i <= 10; i++) {
        if (i == 3) {
            continue;
        } else if (i == 7) {
            break;
        }
        cout << i << endl;
    }

    return 0;
}
```

## Nested Loops
In C++, nexted loops are loops within loops.
The outer most loop dictates how many iterations there are for the inner most loop.
A common naming convention for nested loops is to use `i` as the outer most index and `j` as the inner most index.

```cpp
loop (i = value) {
    ( ... ) // Iterates i times
    loop (j = value) {
        ( ... ) // Iterates i * j times
    }
    cout << "Exiting inner most for loop." << endl;
}
cout << "Exiting outer most for loop." << endl;
```

### Example
```cpp title="20_nested-loops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int row = 3, col = 3;
    char symbol = '@';

    for (int i = 1; i <= row; i++) {
        for (int j = 1; j <= col; j++) {
            cout << symbol;
        }
        cout << endl;
    }

    return 0;
}
```

# `<random>` Library
In C++, the `<random>` standard library is only pseudo-random, meaning it is not truly random but is close enough.

It has two parts that work together to create random numbers:
1. An engine which creates random numbers
2. A distribution which turns them into the kinds of numbers you'd want

For most programs, use a `random_device` to start an `mt19936` engine, and a distribution to get the numbers you need.
- `random_device` creates a random number from the computer, often used as the starting value for the seed
- The Mersenne Twister `mt19937` is a fast, high-quality random number engine

The `<random>` library can be used in conjunction with two other libraries:
- The `<algorithm>` library provides methods to deal with sorting, searching, and manipulating data structures
- The `<ctime>` library provides a variety of functions to measure dates and times

To begin, the `<ctime>` library allows use to seed the `srand()` function with `time(NULL)`, which returns a timestamp resenting the current moment in time.
The `rand()` function will generate a number between 0 and `RAND_MAX`, inclusive, but guaranteed to be at least `32767`. `RAND_MAX` is a constant defined by `<cstdlib>` that gives the largest value the `rand()` function can return.
By using the modulus `&` operator, we can specify a range, and by using the addition `+` operator, we can adjust the starting index of said range.

The second option, uses the `<algorithm>` library, which provides four different distribution functions to seed the engine with:
1. The `uniform_int_distribution<int> range(start, end)` function gives random whole numbers in a range, where every number is equally likely. It includes both values in the parentheses for the range.
2. The `uniform_real_distribution<double> range(start, end)` function gives random decimal numbers in a range, where every number is equally likely. It includes the start index, and excludes the ending index for the range.
3. The `normal_distribution<double> range(mean, stddev)` function gives random decimal numbers in a range, where every number is likely closer to the mean. The first index is the mean and the second index is the standard deviation.
4. The `bernoulli_distribution chance(index)` function gives random boolean values, `true` or `false`, like a coin flip. The index controls how much of the percentage is likely to be `true`

## Example
```cpp title="21_random.cpp"
#include <iostream>
#include <random>
#include <algorithm>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    random_device source;
    mt19937 engine(source());
    uniform_int_distribution<int> die6(1, 6);

    // Roll 4d6, drop the lowest die, add the rest for base stat
    int total = 0;
    int lowest = 7;
    for (int i = 1; i <= 4; i++) {
        int rollD6 = die6(engine);
        cout << "Roll " << i << ": " << rollD6 << endl;
        total += rollD6;
        lowest = min(lowest, rollD6);
    }
    int stat = total - lowest;
    cout << "Stat: " << stat << endl;

    return 0;
}
```

# User Defined Functions
In C++, function are defined as a block of reusable code which executes when called.
C++ provides predefined functions such as the `main()` function which is used as a starting point to execute code.

Users are also able to define their own functions to perform certain actions repetitively.

In C++, the source code is read from the top down, so for readbility's sake, you can declare them before the `main()` method and define them separately afterwards.

To declare a function, specify the `return` value type and the name of the function, followed by paraentheses with parameters.
A return value type describes what data type is expected to be returned by the function using the `return` keyword.
When a function should not return any value, use the `void` return value type.

NOTE: Remember to include default arguments in the declaration to avoid compilation errors.

You can execute code within the function by calling it: `function_name();`.
In C++, there is variable scope, so values in different functions must be passed as paraters when calling functions.
You can set a default parameter value by using the assignment operator `=`.
You are able to pass multiple parameters, so long as you separate them with a comma `,`.
Because the variable is being passed into a different scope, the name can change as need be.

To define a function, write the code block, or the body, to be executed.

## Example
```cpp title="22_userfunctions.cpp"
#include <iostream>
using namespace std;

void happyBirthday(string bdayPerson, int age);

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string name = "Imani";
    int age = 23;

    happyBirthday(name, age);

    return 0;
}

void happyBirthday(string bdayPerson, int age) {
    /// @brief The `happyBirthday()` function prints they happy birthday song to the console
    /// @param bdayPerson The birthday person's name
    /// @param age The birthday person's age
    
    cout << "Inside of happy birthday function.\n" << endl;
    cout << "Happy Birthday to you!" << endl;
    cout << "Happy Birthday dear you!" << endl;
    cout << "Happy Birthday to " << bdayPerson << "!" << endl;
    cout << "Happy Birthday to you!" << endl;
    cout << "You are " << age << " years old!\n" << endl;
}
```

# `return` Keyword

## Example
```cpp title="23_return.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Overloaded Functions

## Example
```cpp title="24_overload-functions.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Variable Scope

## Example
```cpp title="25_variable-scope.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Arrays

## Example
```cpp title="26_single-arrays.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# `sizeof()` Operator

## Example
```cpp title="27_sizeof-ops.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Iteration

## Example
```cpp title="28_iteration.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Pass Array to a Function

## Example
```cpp title="29_pass-array.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Search array for an element

## Example
```cpp title="30_search-array.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# Sort an array

## Example
```cpp title="31_sort-array.cpp"
#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    return 0;
}
```

# `fill()` Function

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

# Fill an array with User Input

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

# Multidimentional Arrays

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

# Memory addresses

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

# Pass by `value` vs. pass by `ref`

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

# `const` Parameters

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

# Pointers

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

# `null` pointers

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

# Dynamic Memory

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

# Recursion

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

# Function Templates

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

# `structs`

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

# Pass `structs` as arguments

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

# `enum`

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

# Object Oriented Programming

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

# Constructors

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

# Constructor Overloading

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

# Getters and Setters

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

# Inheritance

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