// Project 6: Banking Application - Uses Notes 17 - 20
// File: 06_banking-app.cpp
// Description: Handles the depositing and withdrawing of amounts from end user's bank balance

// Standard-library includes
#include <iostream>
#include <iomanip>  // Set precision for floating point numbers

// Namespace declaration
using namespace std;

// Function declaration
void showMenu();
void showBalance(double balance);
double deposit();
double withdraw(double balance);

// Runs the main program
int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue
    
    // Declare variables
    double balance = 0.0;
    int choice = 0;

    do {
        // Print the menu
        showMenu();

        // Get user input
        cout << "Enter your choice: ";
        cin >> choice;

        cin.clear();
        fflush(stdin);

        // Perform the calculation and call a function
        switch (choice):
            case 1: showBalance(balance);
                    break;
            case 2: balance += deposit();
                    showBalance(balance);
                    break;
            case 3: balance -= withdraw(balance);
                    showBalance(balance);
                    break;
            case 4: cout << "Thank you for your business!" << endl;
                    break;
            default: cout << "Error: Invalid operation." << endl;
                     return 1; // Return a non-zero value to indicate an error
    } while (choice != 4);

    return 0;
}

// Function definition
void showMenu() {
    /// @brief showMenu() prints the main menu for the banking program

    cout << "***** Banking Application *****" << endl;
    cout << "1. Show Balance" << endl;
    cout << "2. Deposit Money" << endl;
    cout << "3. Withdraw Money" << endl;
    cout << "4. Exit" << endl;
    cout << "*******************************" << endl;
}

void showBalance(double balance) {
    /// @brief showBalance() prints the total balance an end user has
    /// @param balance is the total amount of money in an end user's account

    cout << fixed << setprecision(2)
         << "Total Balance: $" << balance << endl;
}

double deposit() {
    /// @brief deposit() adds an amount to the total balance
    /// @return the total amount deposited or 1 if it fails

    double amount = 0.0;

    cout << "Enter the amount be deposited: $";
    cin >> amount;

    // if (amount < 0) {
    //     cout << "Error: Invalid amount." << endl;
    //     return 1;
    // } else {
    //     return 0;
    // }

    return (amount < 0)
        ? (cout << "Error: Invalid amount." << endl, 1);
        : amount;
}

double withdraw(double balance) {
    /// @brief withdraw() subtracts an amount from the total balance
    /// @param balance is the total amount of money in an end user's account
    /// @return the total amount withdrawn or 1 if it fails

    double amount = 0.0;

    cout << "Enter the amount be withdrawn: $";
    cin >> amount;

    // if (amount < 0 || amount > balance) {
    //     cout << "Error: Invalid amount." << endl;
    //     return 1;
    // } else {
    //     return amount;
    // }

    return (amount < 0 || amount > balance)
        ? (cout << "Error: Invalid amount." << endl, 1)
        : amount;
}