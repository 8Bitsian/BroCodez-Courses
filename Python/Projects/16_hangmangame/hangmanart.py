# Art for hangman.py

# Dictionary of {key} for incorrect number of guesses and {value} of ASCII art
hangman_art = {0: ("   ",
                   "   ",
                   "   "),  # No wrong answers, no hangman
               1: (" o ",
                   "   ",
                   "   "),  # 1 wrong answer, show head
               2: (" o ",
                   " | ",
                   "   "),  # 2 wrong answers, show torso
               3: (" o ",
                   "/| ",
                   "   "),  # 3 wrong answers, show left arm
               4: (" o ",
                   "/|\\",  # To display the backslash use the escape key
                   "   "),  # 4 wrong answers, show right arm
               5: (" o ",
                   "/|\\",
                   "/  "),  # 5 wrong answers, show left leg
               6: (" o ",
                   "/|\\",
                   "/ \\")  # 6 wrong answers, show right leg
}
