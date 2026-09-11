# File Handling (Detection, Writing, Reading)
import os   # To handle general files, import the operating system `os` module.
import json # To handle `.json` files, import the `.json` module
import csv  # To handle `.csv` files, import the `.csv` module

def check_for_file(file_path):
    # To check whether a path exists and use the `os` module `path.exists` extension, which will return a boolean value depending on if the file is detected.
    if (os.path.exists(file_path)):
        print(f"{file_path} exists!")
        # To check whether a path is a file or directory use the `os` module `path.isfile` extension, which will return a boolean value depending on if the file is detected.
        if os.path.isfile(file_path):
            print("That is a file.")
        elif os.path.isdir(file_path):
            print("That is a directory.")
    else:
        print(f"ERROR: {file_path} not found...")

# To create or overwrite a text file with text and a list of values use the `with` statement to wrap the following code block. When we open a file in the `with` statement, it will automatically close that file when the statement is finished executing.
# The `open()` function will return a file object; The first parameter is the file path and the second parameter is the function mode. There are three modes that are briefly discussed: (1) The write `w` mode, (2) append `a` mode, (3) and read `r` mode. You can set the parameters of the open() function as keyword objects to make them easier to read.
# Close the statement with the `as` keyword to give the following file object an alias.
def write_to_file(file_path, txt_data, collection):
    with open(file=file_path, mode="w") as file:
        # To write to the file, use the `write()` method and a string as an argument
        file.write(txt_data + "\n")
        
        # To write each value within a collection, you'll have to iterate with a loop
        for item in collection:
            # Cast the item in the collection as a string to make it easier to append newline characters to write each value on a newline
            file.write(str(item) + "\n")

        print(f"`{file_path}` was created.")

    # try:
    #     # You can use the `x` mode to write to a file that doesn't exist
    #     with open(file=file_path, mode="x") as file:
    #         file.write(txt_data)
    #         print(f"`{file_path}` was created.")
    # except FileExistsError:
    #     # Since the file does exist, you will get an error message.
    #     print(f"ERROR: Mode Error: `{file_path}` already exists...")

# Append a list, dictionary, or other collection to a file
def append_file(file_path, txt_data, collection):
    # The `isinstance(object, class_info)` method checks the data type of an object
    if (isinstance(collection, dict)):
        # The append `a` mode will insert new data into the file.
        with open(file=file_path, mode="a") as file:
            file.write(txt_data + "\n")
            # The json.dump() extension will print everything on the same line if the indent keyword isn't included
            json.dump(collection, file, indent=4)
            file.write("\n\n")
            print(f"`{file_path}` was updated.")
    elif (isinstance(collection, list) and all(isinstance(row, list) for row in collection)):
        with open(file=file_path, mode="a", newline="") as file:
            # For .csv files create a writer object to provide methods for writing data to a csv file
            writer = csv.writer(file)
            # To write anything to the csv file, we have to iterate over the 2D array
            for row in collection:
                writer.writerow(row)
            file.write("\n")
            print(f"`{file_path}` was updated.")
    else:
        with open(file=file_path, mode="a") as file:
            file.write(txt_data + "\n")
            for item in collection:
                file.write(str(item) + "\n")
            file.write("\n")
            print(f"`{file_path}` was updated.")
