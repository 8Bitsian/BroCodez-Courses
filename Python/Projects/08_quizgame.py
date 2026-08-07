# Project 08: Quiz Game Program - Create a quiz game using 2D array using tuples
# Use 15 Notes
# Create a 

# Tuples are ordered and unchangeable. Duplicates OK. FASTER because data is in fixed positions
# 1D Tuple of questions that the user can answer since these will not change
questions = ("What are the traditional primary colors? ",
             "What color is made by mixing red and blue? ",
             "What color is made by mixing red and yellow? ",
             "What color is made by mixing blue and yellow? ",
             "What are the mixed colors called? ")

# 2D Tuple of 4 options that the user can choose from for each question
# Each element (tuple of options) in options correspond to an element in questions
options = (("A. Red, Green, Blue", "B. Yellow, Orange, Blue", "C. Red, Magenta, Cyan", "D. Magenta, Green, Yellow"),
           ("A. Orange", "B. Green", "C. Purple", "D. Magenta"),
           ("A. Blue", "B. Cyan", "C. Green", "D. Orange"),
           ("A. Red", "B. Green", "C. Orange", "D. Cyan"),
           ("A. Primary", "B. Tertiary", "C. Secondary", "D. Colors"))

# 1D tuple of correct answers
answers = ("A", "C", "D", "B", "C")

# Lists use brackets and are ordered and changeable. Duplicates OK
# List of gueses to keep track of which question was answered
guesses = []

# Initialize a variable to keep score of correct answers  and to track which question we're on
score = 0
q_num = 0

# We can iterate over arrays (both 1D and 2D) via loops and decision structures
# Iterate each element (question) in the questions 1D tuple
for question in questions:
    print("---------------------")
    print(question)
    # Iterate each element (tuple of options) in the options 2D tuple via the index position (q_num)
    for option in options[q_num]:
        print(option)
    
    # Get user input and use the .upper()_ function to normalize their answer
    guess = input("Enter Option (A, B, C, D): ").upper()
    # Use the .append() function to add the user input to the end of the guesses list
    guesses.append(guess)

    # Check user input and increase score if guess is equal to answer element via the index position (q_num)
    if guess == answers[q_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[q_num]} is the correct answer...")
    q_num += 1

# Exit the loop after user enters all of the questions
print("---------------------")
print("       RESULTS       ")
print("---------------------")

# Iterate over all of the answers and the guesses
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("gueses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")