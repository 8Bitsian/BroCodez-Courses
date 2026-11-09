/*
    In C++, the ternary operator `?:` is a shorthand way to write an if-else statement.
    It has the syntax: `condition ? value_if_true : value_if_false`.
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int grade = 75;

    /*
        if (grade >= 60) {
            cout << "You passed!" << endl;
        } else {
            cout << "You failed." << endl;
        }
    */

    // Using the ternary operator
    (grade >= 60) ? cout << "You passed!" << endl : cout << "You failed." << endl;


    int number = 9;

    /*
        if (number % 2 == 0) {
            cout << "The number is even." << endl;
        } else {
            cout << "The number is odd." << endl;
        }
    */

    // Using the ternary operator
    (number % 2 == 0) ? cout << "The number is even." << endl : cout << "The number is odd." << endl;


    bool isRaining = true;

    /*
        if (isRaining) {
            cout << "It is raining." << endl;
        } else {
            cout << "It is not raining." << endl;
        }
    */

    // Using the ternary operator
    //(isRaining) ? cout << "It is raining." << endl : cout << "It is not raining." << endl;

    // Another example using the ternary operator
    cout << (isRaining ? "Take an umbrella." : "No need for an umbrella.") << endl;

    return 0;
}