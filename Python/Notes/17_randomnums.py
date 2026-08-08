# Random Numbers - To generate random numbers import the random library module
import random

# For a list of all of the methods use the help method print(help(random))

# The following is a list of methods availble to the random library
# The .randint(start, end) method prints random integers within a range that is inclusive
dice6 = random.randint(1, 6)
print(dice6)

# For D&D you can create a bunch of random dices
dice21 = random.randint(1, 21)
print(dice21)

# You can use integer variables in the range
low = 1
high = 100
dice100 = random.randint(low, high)
print(dice100)

# The .random(start, end) method prints random floating-points within a range of 0 and 1 that is inclusive
number = random.random()
print(f"{number:.5f}")

# The .choice(seq) method prints a random elemnt from a list or a sequence
# For rock, paper, scissors, create a tuple
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

# The .shuffle(seq) method reorders the values of elements per indexes
# For shuffling a 52 deck of cards
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]
print(cards)
random.shuffle(cards)
print(cards)