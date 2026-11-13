// Project 4: Random Event Generator - Uses Notes 14 - 16
// File: 04_random-event.cpp
// Description: Generates a random event based on a random number generator

// Standard-library includes
#include <iostream>
#include <algorithm>
#include <random>

// Namespace declaration
using namespace std;

// Runs the main program
int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    // Declare random number generator
    random_device source;
    mt19937 engine(source());
    uniform_int_distribution<int> event(1, 5);

    // Declare variables
    int randNum = event(engine);

    // Print the header
    cout << "***** Random Event Generator *****" << endl;

    // Perform the calculation and output the resule
    switch (randNum) {
        case 1: cout << "You win a bumper sticker." << endl;
                break;
        case 2: cout << "You win a t-shirt." << endl;
                break;
        case 3: cout << "You win a free lunch." << endl;
                break;
        case 4: cout << "You win a gift card." << endl;
                break;
        case 5: cout << "You win a concert ticket." << endl;
                break;
    }
    
    return 0;
}