/*
    In C++, functions are considered a block of reusable code which executes when called.
    C++ provides pre-defined functions, such as `main()`, which is used as a starting point to execute code.
    You can also define your own functions to perform certain actions.
*/

#include <iostream>
using namespace std;

/*
    In C++, the source code is read from the top down, so a way to create user-defined functions for better readbility is to declare them and define them separately.

    To declare a function, specify the return value type and the name of the function, followed by parentheses.
    Return values describe what data type is expected to be returned by the function using the `return` keyword.
    To declare that a function should not return a value, use the `void` return value type.

    Default arguments go in the declaration
*/
void function_name();
void happyBirthday(string bdayPerson, int age);

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string name = "Imani";
    int age = 23;

    cout << "Inside of main function\n" << endl;
    function_name();    // Execute code within the user defined function by calling it
    cout << "Inside of main function\n" << endl;
    // C++ has variable scope, so values in different functions must be passed when funcitons are invoked.
    // You can pass multiple variable to the function
    happyBirthday(name, age);    
    cout << "Inside of main function" << endl;

    return 0;
}

void function_name() {
    // To define a function, write the body of the function, or code to be executed
    cout << "Inside of user defined function.\n" << endl;
}

/*
    Information can be passed to function as parameters, which act as variables within the function.
    You can set a default parameter value by using the assignment operator `=`.
    Because the variable is being passed into a different scope, the name can change as need be
*/

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