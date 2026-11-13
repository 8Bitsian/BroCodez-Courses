/*
    In C++, the `<random>` standard library is only pseudo-random, meaning it is not truly random but is close enough.
    It has two parts that work together to create random numbers:
        1. An engine which creates random numbers
        2. A distribution which turns them into the kinds of numbers you'd want
    For most programs, use a `random_device` to start an `mt19936` engine, and a distribution to get the numbers you need.
*/

#include <algorithm>    // The `<algorithm>` library provides methods to deal with sorting, searching, and manipulating data structures
#include <iostream>     // The `<iostream>` library provides methods which can read user input and output data to the console or a file
#include <random>       // The `<random>` library creates random numbers
#include <ctime>

using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    random_device source;       // Creates a random number from the computer, often used as the starting value for the seed
    mt19937 engine(source());   // The Mersenne Twister `mt19937` is a fast, high-quality random number engine

    // `uniform_int_distribution` gives random whole numbers in a range, where every number is equally likely
    uniform_int_distribution<int> die6(1, 6); // Includes both values in the range
    int roll = die6(engine);
    cout << roll << endl;

    // `uniform_real_distribution` gives random decimal numbers in a range
    uniform_real_distribution<double> unit(0.0, 1.0); // Includes first value, excludes last value
    double value = unit(engine);
    cout << value << endl;

    // `normal_distribution` gives random decimal numbers in a range, where every number is closer to an average value (mean)
    normal_distribution<double> normal(100.0, 15.0); // The first value is the mean, and the second is the standard deviation
    double sample = normal(engine);
    cout << sample << endl;

    // Gives random boolean values `true` or `false`, like a coin flip
    bernoulli_distribution coin(0.5); // The value controls how much of the percentage is likely to be `true`
    bool toss = coin(engine);
    cout << toss << endl;

    // Another way to use random number generators is to use the standard `rand()` funtion
    srand(time(NULL));  // Used to seed the random number generator

    cout << RAND_MAX << endl; // RAND_MAX is a constant defined by `<cstdlib>` that gives the largest value the `rand()` function can return

    int num = rand();   // The `rand()` function will generate a number between 0 and `RAND_MAX`, inclusive, but guarnteed to be at least `32767`
    cout << num << endl;

    int range = rand() % 500; // By using the modulus `&` operator, we can specify a range (in this case is 0 - 499)
    cout << range << endl;

    int dice = (rand() % 6) + 1; // To have the range start at index 1, simply add 1 (in this case is 1 - 6)
    cout << dice << endl;

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