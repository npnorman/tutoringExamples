# Nicholas Norman November 2025
# Goal: Showcase how CSV can be used to open files and save files

# To use the csv reader and writer, we need to import that library
import csv

# First, we want to read in the data. We can see what the data looks like too.
# We can use the 'with' keyword with 'open' to make file reading easier

# This variable is set to a file type, it isa special data type that is an object
file = open("./data/student-data.csv", "r") # r is for read mode

with file:
    # we can work with our file here
    lines = []

    # a reader is another special data type that is used for making csv's easier to read
    reader = csv.reader(file)

    # Now we want to iterate through each row,
    # Let's see what it looks like...
    for row in reader:
        print("Row: ", row)

        # we also should save this to work with later
        lines.append(row)