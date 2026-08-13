# Project 15: Encryption Program - Uses Notes 18-28
# Create a substitution cipher encryption program to hide message by parsing and replacing characters of strings

import random
import string

def encrypt_string(chars, keys):
    plain_text = input("\nEnter Message for Encryption: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += keys[index]

    print(f"Original Message:  {plain_text}")
    print(f"Encrypted Message: {cipher_text}\n")

def decrypt_string(chars, keys):
    cipher_text = input("\nEnter Message for Decryption: ")
    plain_text = ""

    for letter in cipher_text:
        index = keys.index(letter)
        plain_text += chars[index]

    print(f"Encrypted Message: {cipher_text}")
    print(f"Original Message:  {plain_text}\n")

def menu():
    print("~~~~~~~ SECURITY LAYER ~~~~~~~")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def main():
    # chars = "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)

    is_running = True

    # If is_running = False, exit the while loop
    while is_running:
        # Call the menu() function
        menu()

        # Typecasting as an integer and using exeception handling
        try: 
            choice = int(input("Enter Menu Option: "))

            if (choice < 1 or choice > 3):
                print("ERROR: Out of Range - Value in between (1-3)\n")
                continue
        except:
            print("ERROR: Invalid Input - Single digits only (1-3)\n")
            continue
        
        match (choice):
            case 1:
                # Call the encrypt_string() function
                encrypt_string(chars, keys)
            case 2:
                # Call the decrpyt_string() function
                decrypt_string(chars, keys)
            case 3:
                # Exit the loop
                is_running = False
    
    print("\nExiting program...")

# The program starts by checking if filename is main
if __name__ == "__main__":
    main()