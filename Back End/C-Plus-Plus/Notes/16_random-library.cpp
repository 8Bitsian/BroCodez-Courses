/*
    In C++, the `<random>` standard library is only pseudo-random, meaning it is not truly random but is close enough.
*/

#include <iostream>
#include <random>
#include <ctime>

using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    srand(time(NULL));  // Used to seed the random number generator

    int num = rand();   // This will generate a number between 1 and 32,667
    cout << num << endl;

    int range = rand() % 500; // By using the modulus `&` operator, we can specify a range (in this case is 0 - 499)
    cout << range << endl;

    int dice = (rand() % 6) + 1; // To have the range start at index 1, simply add 1 (in this case is 1 - 6)
    cout << dice << endl;

    int d4 = (rand() % 4) + 1;  // Small weapon damage, some spells
    int d6 = (rand() % 6) + 1;  // Light weapon damage, character stats
    int d8 = (rand() % 8) + 1;  // Medium weapon damage, some spells
    int d10 = (rand() % 10) + 1;    // Large weapon damage, hit points
    int d12 = (rand() % 12) + 1;    // Heavy weapon damage, class hit dice
    int d20 = (rand() % 20) + 1;    // Attack rolls, svaing throws, ability checks
    int d100 = (rand() % 100) + 1;  // Percentile dice for random outcomes and loot tables

    cout << d4 << " " << d6 << " " << d8 << " " << d10 << " " << d12 << " " << d20 << " " << d100 << endl;

    // Roll 4d6, drop the lowest die, add the rest for base stat
    int total = 0, lowest = 7;
    for (int i = 1; i <= 4; i++) {
        int rollD6 = (rand() % 6) + 1;
        cout << "Roll " << i << ": " << rollD6 << endl;
        total += rollD6;
        lowest = min(lowest, rollD6);
    }
    int stat = total - lowest;
    cout << "Stat: " << stat << endl;

    return 0;
}