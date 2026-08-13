# Exercise 07: Credit Card Parser - Uses Note 9
# Get the last 4 digits of a credit card number using string indexing.

credit_card = input("Enter a credit card number: ")

last_digits = credit_card[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")
