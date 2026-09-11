# File Detection

# To handle files, import the operating system `os` module.
import os

def check_for_file(file_path):
    # To check if a file exists use the os module path exists extension, which will return a boolean value depending on if the file is detected.
    if (os.path.exists(file_path)):
        print(f"{file_path} exists!")

        # You can check if the file path leads to a file and not a directory using the `isfile` module extension
        if os.path.isfile(file_path):
            print("That is a file.")
        elif os.path.isdir(file_path):
            print("That is a directory.")
    else:
        print(f"ERROR: {file_path} not found...")

def main():
    # To detect certain files use a string w/a relative h (Ex. folder/test.txt) or an absolute file path (Ex. C:Usrs/BroCodez/Desktop/test.txt).
    # When referencing a file, type the file's name and extension as a string (Ex. "test.txt").
    
    # The `r` prior to the string indicates a raw string which correct any combatant backslashes that can be interpretted as escape characters.
    file_path = r"Python\Notes\42_filehandling\text.txt"

    # Another way would be to rewrite the file direcotry using forward slashes `/` instead of backwards slashes `\` to avoid conflicts with escape characters.
    # file_path = "Python/Notes/42_filehandling/text.txt"

    # Call the access_module function
    check_for_file(file_path)

if __name__ == "__main__":
    # print(f"Called main.py file is: {__name__}\n")
    main()
    # print("Exiting main.py file...")