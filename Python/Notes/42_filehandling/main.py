# File Handling (Detection, Writing, Reading)
# When writing to files we can use the extensions `.txt`, `.json`, and `.csv`
import os   # To handle general files, import the operating system `os` module.
import json # To handle `.json` files, import the `.json` module
import csv  # To handle `.csv` files, import the `.csv` module

from file_handling import (check_for_file, write_to_file, append_file)
from text_data import (TXT_DATA_1, TXT_DATA_2, TXT_DATA_3)
from collections import (DREAMHOUSE, WARHAMMER_40K, GUNDAM_ZERO, TRANSFORMERS)

def main():
    # To detect certain files use a string w/a relative h (Ex. folder/test.txt) or an absolute file path (Ex. C:Usrs/BroCodez/Desktop/test.txt).
    # When referencing a file, type the file's name and extension as a string (Ex. "test.txt").
    
    # The `r` prior to the string indicates a raw string which correct any combatant backslashes that can be interpretted as escape characters.
    file_path = r"Python\Notes\42_filehandling\text.txt"

    # Another way would be to rewrite the file direcotry using forward slashes `/` instead of backwards slashes `\` to avoid conflicts with escape characters.
    # file_path = "Python/Notes/42_filehandling/text.txt"

    # Call the check_for_file() function
    check_for_file(file_path)
    
    # Call the write_to_file function
    write_to_file(file_path, TXT_DATA_1, DREAMHOUSE)

    # Call the append_file function
    append_file(file_path, TXT_DATA_2, WARHAMMER_40K)
    append_file(file_path, TXT_DATA_3, GUNDAM_ZERO)
    append_file(file_path, TXT_DATA_3, TRANSFORMERS)

if __name__ == "__main__":
    main()
