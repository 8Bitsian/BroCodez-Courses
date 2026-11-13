// Project 5: Number Guessing Game - Uses Notes 14 - 16
// File: 05_number-guess-game.cpp
// Description: User guesses a mystery value from a random number generator

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
    uniform_int_distribution<int> value(1, 100);

    // Declare variables
    int randNum = value(engine);
    int guess, tries;

    // Print the header
    cout << "***** Number Guessing Game *****" << endl;

    do {
        cout << "Enter a guess between (1-100): ";
        cin >> guess;
        tries++;

        // Perform the calculation and output the result
        if (guess > randNum) {
            cout << "Too high!" << endl;
        } else if (guess < randNum) {
            cout << "Too low!" << endl;
        }

    } while (guess != randNum);
    cout << "********************************" << endl;
    cout << "CORRECT! # of attempts: " << tries << endl;
    
    return 0;
}