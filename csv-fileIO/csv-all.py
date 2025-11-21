# Nicholas Norman November 2025
# Goal: Showcase how CSV can be used to open files and save files

# To use the csv reader and writer, we need to import that library
import csv

# First, we want to read in the data. We can see what the data looks like too.
# We can use the 'with' keyword with 'open' to make file reading easier

# This variable is set to a file type, it isa special data type that is an object
file = open("./data/student-data.csv", "r") # r is for read mode

# we can work with our file here
lines = []

with file:
    # a reader is another special data type that is used for making csv's easier to read
    reader = csv.reader(file)

    # Now we want to iterate through each row,
    # Let's see what it looks like...
    for row in reader:
        # we also should save this to work with later
        lines.append(row)

###############################################################
# We can manipulate the lines, then below it saves it.
# This is where you may calculate some values or change values
# Add or remove rows/columns

for i in range(1,len(lines)):
    lines[i][4] = float(lines[i][4])
    lines[i][4] = lines[i][4] / 3.281

    lines[i][4] = round(lines[i][4], 2)

###############################################################

# This variable is set to a file type, it isa special data type that is an object
file = open("./data/modified-student-data.csv", "w", newline='') # w is for write mode, newline='' removes spaces between lines

with file:

    # a writer is another special data type that is used for making csv's easier to write to
    writer = csv.writer(file)

    # we can continue to write the data
    writer.writerows(lines)