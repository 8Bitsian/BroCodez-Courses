/*
    In C++, function overloading allows multiple functions to have the same name so long as their parameters are different in data type or number.
    Instead of defining two functions that should do the same thing, it is better to overload one.
    This lets you use the same function name for similar tasks.
*/

#include <iostream>
using namespace std;

int addFunc(int x, int y);
double addFunc(double x, double y);

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int numInt = addFunc(8, 5); // A function name and paramters is called a function signature, and is used to identify the function
    double numDouble = addFunc(4.0, 9.2);

    cout << "   Int: " << numInt << endl;
    cout << "Double: " << numDouble << endl;

    return 0;
}

int addFunc(int x, int y) {
    /// @brief Adding two variables together
    /// @param x, y Two values to add together
    /// @return Sum of values

    return x + y;
}

double addFunc(double x, double y) {
    /// @brief Adding two variables together
    /// @param x, y Two values to add together
    /// @return Sum of values

    return x + y;
}