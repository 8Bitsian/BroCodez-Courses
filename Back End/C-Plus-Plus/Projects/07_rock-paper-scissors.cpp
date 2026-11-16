// Project 7: Rock, Paper, Scissors - Uses Notes 17 - 20
// File: 07_rock-paper-scissors.cpp
// Description: Generate choice of rock paper scissors and display

// Standard-library includes
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <random>
#include <ctime>

// Namespace declaration
using namespace std;

// Function declaration
void showMenu();
int getUserInput();
int getCompInput();
void showChoice(int choice);
void chooseWinner(int player, int computer);

// Runs the main program
int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue
    
    // Declare variables
    int player = 0;
    int computer = 0;
    int choice = 0;

    cout << "***** Rock, Paper, Scissors *****" << endl;

    do {
        // Call functions
        player = getUserInput();
        computer = getCompInput();

        // Print output
        cout << "Player Choice: ";
        showChoice(player);
        cout << "Computer Choice: ";
        showChoice(computer);

        // Print output
        chooseWinner(player, computer);

        cout << "Play again? (1 or 2): ";
        cin >> choice;
    } while (choice != 2)

    return 0;
}

// Function definition
void showMenu() {
    /// @brief showMenu() prints the main menu for the rock, paper, scissors game

    cout << "Choose a hand to play:" << endl;
    cout << "1. Rock" << endl;
    cout << "2. Paper" << endl;
    cout << "3. Scissors" << endl;
    cout << "*************************" << endl;
}

int getUserInput() {
    /// @brief getUserInput() prints the main menu and gets the end user input for hand choice
    /// @return the end user's choice of rock, paper, or scissors as 1, 2, or 3

    int player;

    do {
        showMenu(); // Print the menu
        // Get user input
        cout << "Enter your choice: ";
        cin >> player;
    } while (player != 1 && player != 2 && player != 3);

    return player;
}

int getCompInput() {
    /// @brief getCompInput() generates a random number between 1 and 3 to pick the bot's hand choice
    /// @return the computer's choice of rock, paper, or scissors as 1, 2, or 3

    // Declare random number generator
    random_device source;
    mt19937 engine(source());
    uniform_int_distribution<int> hand(1, 3);

    // Declare variables
    int randNum = event(engine);

    return randNum;
}

void showChoice(int choice) {
    /// @brief showChoice() shows the hands each player chose
    /// @param choice is the player/computer choice hand

    switch (choice) {
        case 1: cout << "Rock" << endl;
                break;
        case 2: cout << "Paper" << endl;
                break;
        case 3: cout << "Scissors" << endl;
                break;
    }

}

void chooseWinner(int player, int computer) {
    /// @brief chooseWinner() determines who won round of game
    /// @param player is the player's choice hand
    /// @param computer is the computer's generated hand

    switch(player) {
        case 1: if (computer == 1) { cout << "Its a tie." << endl; }
                else if (computer == 2) { cout << "You lose..." << endl; }
                else { cout << "You win!" << endl; }
                break;
        case 2: if (computer == 2) { cout << "Its a tie." << endl; }
                else if (computer == 3) { cout << "You lose..." << endl; }
                else { cout << "You win!" << endl; }
                break;
        case 3: if (computer == 3) { cout << "Its a tie." << endl; }
                else if (computer == 1) { cout << "You lose..." << endl; }
                else { cout << "You win!" << endl; }
                break;
    }
}