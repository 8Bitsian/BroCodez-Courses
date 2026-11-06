/*
    A variable is a named storage location in memory that can hold a value of a specific data type. In C++, variables are used to store and manipulate data during the execution of a program.
    There are two steps to creating a variable in C++:
        1. Declare the variable's data type and name (identifier)
        2. Initialize the variable with a value (optional, but recommended)
    The data type of a variable determines the kind of data it can hold, such as integers, floating-point numbers, characters, or more complex types like arrays and objects.
*/

#include <iostream>
#include <string> // The `<string>` header file is included to use the `std::string` class, which allows you to work with strings in C++.
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    /*
        Each variable has a unique name (identifier) and a data type that determines the kind of data it can hold.
        There are different data types in C++ that you can use to store different kinds of data. Some common data types include:
        - `int`: Used to store whole numbers (e.g., 1, -5, 100)
        - `float`: Used to store decimal numbers (e.g., 3.14, -0.5, 2.718)
        - `double`: Used to store double-precision decimal numbers (e.g., 3.14159, -0.0001, 2.71828)
        - `char`: Used to store single characters (e.g., 'a', 'Z', '1')
        - `bool`: Used to store boolean values ('true' or 'false')
    */

    // To store a whole number, you can use the `int` data type. The `int` data type is used to represent integer values, which are whole numbers without any decimal points.
    int age; // When assigning a data type to a variable, you are declaring the variable. In this case, we are declaring a variable named `age` of type `int`.
    age = 23; // When assigning a value to a variable, you are initializing the variable. In this case, we are initializing the variable `age` with the value 23

    int year = 2003; // You can also declare and initialize a variable in a single line of code.

    int days = 7.5; // Since `days` is declared as an integer variable, the decimal part (.5) will be truncated, and the value of `days` will be 7.

    cout << "I am " << age << " years old." << endl; // Pay attention to the `<<` operator, which is used to concatenate (combine) multiple values and strings together for output, and include a space between the words and the variable value.
    cout << "I was born in " << year << "." << endl;
    cout << "My birthday is in " << days << " days." << endl;

    float pi = 3.14159; // The `float` data type is used to store decimal numbers (floating-point numbers).

    cout << "Pi is approximately " << pi << "." << endl;

    double e = 2.71828; // The `double` data type is used to store double-precision decimal numbers.
    double gpa = 2.5;
    double temperature = 98.6;

    cout << "E is approximately " << e << "." << endl;
    cout << "My GPA is " << gpa << "." << endl;
    cout << "The temperature is " << temperature << " degrees." << endl;

    bool isRaining = false; // The `bool` data type is used to store boolean values, which can be either `true` or `false`.
    bool isSunny = true;

    cout << "Is it raining? " << isRaining << endl; // When printing a boolean variable, `false` is represented as 0 and `true` is represented as 1.
    cout << "Is it sunny? " << isSunny << endl;

    char grade = 'A'; // The `char` data type is used to store single characters, which include letters (a-z, A-Z), digits (0-9), and special characters.
    char initial = '8b'; // It can be overloaded, though it isn't recommended, and will store multiple characters, but it will only print the last character `b`.
    char currency = '$'; // The `char` data type can also be initialized with the nonalphabetic characters, such as `$`, `@`, `#`, etc.
    
    cout << "My grade is " << grade << "." << endl;
    cout << "My initial is " << initial << "." << endl;
    cout << "My currency symbol is " << currency << "." << endl;

    // `string` is not a primitive data type; it is an object that is used to store a sequence of characters (text).
    // The `string` object is part of the C++ Standard Library, and it provides various functions and methods to manipulate strings.

    string name = "8BitSoftware"; // The `string` objects are declared the same way as the primitive data types. In this case, we are declaring a variable named `name` of type `string` and initializing it with the value "BroCode".
    string address = "123 Main St"; // You can also declare and initialize a `string` object in a single line of code.
    string city = "New York"; // You can also declare and initialize a `string` object with spaces in the value.
    // string country;   You can also declare a `string` object without initializing it.

    cout << "My name is " << name << "." << endl;
    cout << "I live at " << address << "." << endl;
    cout << "I live in " << city << "." << endl;

    return 0;
}