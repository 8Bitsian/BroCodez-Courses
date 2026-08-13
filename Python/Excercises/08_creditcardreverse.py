# Exercise 08: Reverse Credit Card - Notes 9
# Reverse the order of the credit card number using string indexing

credit_card = input("Enter a credit card number: ")

# To reverse a string set the step to be negative
reverse_digits = credit_card[::-1]

print(f"{reverse_digits}")
