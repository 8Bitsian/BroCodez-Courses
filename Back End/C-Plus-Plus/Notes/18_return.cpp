/*
    The `return` keyword returns a value back to the spot where the encompassing function was called.
*/

#include <iostream>
using namespace std;

double getLength();
double calcSquareArea(double length);
double calcCubeVolume(double length);
void printOutput(double sArea, double cVolume);

string getName();
string concatStrings(string fName, string lName);
void printName(string fullName);

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    double length = getLength();
    double sArea = calcSquareArea(length);
    double cVolume = calcCubeVolume(length);

    printOutput(sArea, cVolume);

    string fName = getName();
    string lName = getName();
    string fullName = concatStrings(fName, lName);

    printName(fullName);

    return 0;
}

double getLength() {
    /// @brief Get the user input for length of a square
    /// @return result
    double result;

    cout << "Enter a value: ";
    cin >> result;
    
    return result;
}

double calcSquareArea(double length) {
    /// @brief Calcalates the area of a square
    /// @param length   Length in units of a square
    /// @return area of a square
    
    return length * length;
}

double calcCubeVolume(double length) {
    /// @brief Calcalates the volume of a cube
    /// @param length   Length in units of a cube face (square)
    /// @return volume of a cube
    
    return length * length * length;
}

void printOutput(double sArea, double cVolume) {
    /// @brief Ouputs the area of a square and the volume of a cube
    /// @param sArea    Area of a square
    /// @param sVolume  Volume of a cube

    cout << endl;
    cout << "   Area of the square: " << sArea << " units²" << endl;
    cout << "   Volume of the cube: " << cVolume << " units³\n" << endl;
}

string getName() {
    /// @brief Get the user input for their name
    /// @return name
    string name;

    cout << "Enter name: ";
    cin >> name;
    
    return name;
}

string concatStrings(string fName, string lName) {
    /// @brief Concatenates a user's first and last name into a string
    /// @param fName    User's first name
    /// @param lName    User's last name
    /// @return full name

    return fName + " " + lName;
}

void printName(string fullName) {
    /// @brief Outputs the end user's full name in a string
    /// @param fullName End user's full name

    cout << endl;
    cout << "   Your full name: " << fullName << endl << endl;
}