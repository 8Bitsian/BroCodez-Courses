# File Handling (Detection, Writing, Reading)
import os   # To handle general files, import the operating system `os` module.
import json # To handle `.json` files, import the `.json` module
import csv  # To handle `.csv` files, import the `.csv` module

def txt_data():
    # When writing to files we can use the extensions `.txt`, `.json`, and `.csv`
    txt_data1 = "I like dolls."
    txt_data2 = "I also like action figures!"
    txt_data3 = "Models are also pretty fricken sweet!"

def collections():
    # This list is what I initialize the text.txt file with
    dreamhouse = ["Barbara", "Kenneth", "Nikki", "Raquelle", "Summer", "Ryan"]

    # I append the original text.txt file with the remaining collections
    warhammer40K = ["Imperium of Man", "Eldar", "Tyranids", "Orks", "Necrons", "T'au Empire"]

    # `.json` files are made w/key value pairs, like dictionaries are.
    gundam = {
        "designation": "Gundam ZERO",
        "model #": "XARX-0",
        "pilot": "Ray Azumi",
    }

    # Comma separated value `.csv` files are made like excel spreadsheets, like 2D arrays are.
    transformers = [["Designation", "Faction", "Position", "Frame", "Generation"],
                    ["Starscream", "Decepticon", "SIC and Air Commader", "Seeker", 1],
                    ["Sunstreaker", "Autobot", "Frontrunner", "Grounder", 1],
                    ["Bluestreak", "Autobot", "Sniper", "Grounder", 1]]

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

def write_to_file(file_path, txt_data, dreamhouse):
    # To create a file object with the `with` statement to wrap the following code block. When we open a file in the `with` statement, it will automatically close that file when the statement is finished executing.

    # The `open()` function will return a file object; The first parameter is the file path and the second parameter is the function mode. There are three modes that are briefly discussed: (1) The write `w` mode, (2) append `a` mode, (3) and read `r` mode. You can set the parameters of the open() function as keyword objects to make them easier to read.

    # Close the statement with the `as` keyword to give the following file object an alias.
    with open(file=file_path, mode="w") as file:
        # To write to the file, use the `write()` method and a string as an argument
        file.write(txt_data + "\n")
        # To write each value within a collection, you'll have to iterate with a loop
        for doll in dreamhouse:
            # To write each value on a newline, append a newline character to the end
            file.write(doll + "\n")

        print(f"`{file_path}` was created.")

    try:
        # You can use the `x` mode to write to a file that doesn't exist
        with open(file=file_path, mode="x") as file:
            file.write(txt_data)
            print(f"`{file_path}` was created.")
    except FileExistsError:
        # Since the file does exist, you will get an error message.
        print(f"ERROR: Mode Error: `{file_path}` already exists...")

def append_file(file_path, txt_data, collection):
    # Syntax of an isinstance() method is object, class_info
    if (isinstance(collection, dict)):
        # The append `a` mode will add new data into the file.
        # To insert data into a new line, insert a new line character
        with open(file=file_path, mode="a") as file:
            file.write(txt_data + "\n")
            # The json.dump() extension will print everything on the same line if the indent keyword isn't included
            json.dump(collection, file, indent=4)
            print(f"`{file_path}` was updated.")
    elif (isinstance(collection, list)):
        with open(file=file_path, mode="a", newline="") as file:
            # For .csv files create a writer object to provide methods for writing data to a csv file
            writer = csv.writer(file)
            # To write anything to the csv file, we have to iterate over the 2D array
            for row in collection:
                writer.writerow(row)
            print(f"`{file_path}` was updated.")
    else:
        with open(file=file_path, mode="a") as file:
            file.write(txt_data + "\n")
            for figure in collection:
                file.write(figure + "\n")
            print(f"`{file_path}` was updated.")