// Project 3: Temperature Converter - Uses Notes 11 - 13
// File: 03_temperature-converter.cpp
// Description: Converts the fahrenheit temperature to celsius and vice versa.

// Standard-library includes
# include <iostream>

// Namespace declaration
using namespace std;

// Runs the main program
int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue
    
    // Declare variables
    char unit;
    double temp, celsius, fahrenheit;

    // Print the menu
    cout << "***** Temperature Converter *****" << endl;
    cout << "F = Fahrenheit" << endl;
    cout << "C = Celsius" << endl;

    // Get user input for the operation
    cout << "Enter the unit to convert to: ";
    cin >> unit;

    // Get user input for the temperature
    cout << "Enter the temperature: ";
    cin >> temp;

    // Perform the calculation based on the operation
    switch (unit) {
        case 'F':   // Convert celsius to fahrenheit
        case 'f':
            fahrenheit = (1.8 * temp) + 32.0;
            cout << "Result: " << fahrenheit << "°F" << endl;
            break;
        case 'C':   // Convert fahrenheit to celsius
        case 'c':
            celsius = (temp - 32.0) / 1.8;
            cout << "Result: " << celsius << "°C" << endl;
            break;
        default:
            cout << "Error: Invalid operation." << endl;
            return 1; // Return a non-zero value to indicate an error
    }

    return 0;
}