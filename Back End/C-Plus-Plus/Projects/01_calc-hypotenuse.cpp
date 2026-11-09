// Project 1: Calculate Hypotenuse - Uses Notes 1 - 9
// File: 01_calc-hypotenuse.cpp
// Description: Demonstrates how to calculate the hypotenuse of a right triangle using the Pythagorean theorem (H = a^2 + b^2) and the `<cmath>` library for mathematical operations.

// Standard-library includes
# include <iostream>
# include <cmath>

// Namespace declaration
using namespace std;

// Runs the main program
int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue
    
    // Define variables
    double side_a, side_b, hypotenuse;

    // Get user input
    cout << "Enter the length of side A: ";
    cin >> side_a;
    cout << "Enter the length of side B: ";
    cin >> side_b;

    // Process the input (H = a^2 + b^2)
    hypotenuse = sqrt(pow(side_a, 2) + pow(side_b, 2));

    // Output the results
    cout << "The length of the hypotenuse is: " << hypotenuse << "² units" << endl;

    return 0;
}