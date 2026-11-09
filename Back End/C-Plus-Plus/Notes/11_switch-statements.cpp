/*
    In C++, `switch` statements are another decision structure that act as an alternative to multiple `if else` statements.
    They are used when you have a variable that can take on multiple discrete values.
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int month;
    cout << "Enter a month number (1-12): ";
    cin >> month;

    switch (month) {
        case 1:
            cout << "It is January";
            break;  // The `break` statement is used to exit the switch statement after a case has been executed.
        case 2:
            cout << "It is February";
            break;
        case 3:
            cout << "It is March";
            break;
        case 4:
            cout << "It is April";
            break;
        case 5:
            cout << "It is May";
            break;
        case 6:
            cout << "It is June";
            break;
        case 7:
            cout << "It is July";
            break;
        case 8:
            cout << "It is August";
            break;
        case 9:
            cout << "It is September";
            break;
        case 10:
            cout << "It is October";
            break;
        case 11:
            cout << "It is November";
            break;
        case 12:
            cout << "It is December";
            break;
        default:
            cout << "Invalid month number (1-12).";
    }

    return 0;
}