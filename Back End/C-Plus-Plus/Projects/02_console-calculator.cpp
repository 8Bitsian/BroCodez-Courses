// Project 2: Console Calculator - Uses Notes 9 - 11
// File: 02_console-calculator.cpp
// Description: Demonstrates a simple console calculator that performs basic arithmetic operations based on user input. The program prompts the user to enter an operation and two numbers, then calculates and displays the result.

// Standard-library includes
#include <iostream>

// Namespace declaration
using namespace std;

// Runs the main program
int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    // Declare variables
    char operation;
    double num1, num2, result;

    cout << "*** Welcome to the Console Calculator ***" << endl;

    // Get user input for the operation
    cout << "Enter an operation (+, -, *, /): ";
    cin >> operation;

    // Get user input for the numbers
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;

    // Perform the calculation based on the operation
    switch (operation) {
        case '+':
            result = num1 + num2;
            cout << "Result: " << result << endl;
            break;
        case '-':
            result = num1 - num2;
            cout << "Result: " << result << endl;
            break;
        case '*':
            result = num1 * num2;
            cout << "Result: " << result << endl;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                cout << "Result: " << result << endl;
            } else {
                cout << "Error: Division by zero is not allowed." << endl;
                return 1; // Return a non-zero value to indicate an error
            }
            break;
        default:
            cout << "Error: Invalid operation." << endl;
            return 1; // Return a non-zero value to indicate an error
    }

    return 0;
}