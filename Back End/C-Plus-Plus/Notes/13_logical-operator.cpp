/*
    In C++, logical operators are used to compare multiple conditions. There are three kinds of logical operators:
        1. The and operator `&&` checks if two or more conditions are `true`
        2. The or operator `||` checks if at least one of two or more conditions are `true`
        3. The not operator `!` reverses the logical state of its operand
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int temperature;
    bool isSunny = true;

    cout << "Enter the temperature (°C): ";
    cin >> temperature;

    // The AND logical operator checks if two conditions are `true`
    if (temperature > 0 && temperature < 30) { 
        cout << "The temperature is nice." << endl;
    // The OR logical operator checks if one of two conditions are `true`
    } else if (temperature <= 0 || temperature >= 30) {
        cout << "The temperature is bad." << endl;
    } else {
        cout << "Invalid input." << endl;
    }

    // The NOT logical operator checks the inverse of a condition
    if (!isSunny) { // Same syntax as `isSunny != true` or NOT equal to
        cout << "It will rain." << endl;
    } else {
        cout << "It is sunny." << endl;
    }

    return 0;
}