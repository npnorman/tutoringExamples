# Nicholas Norman November 2025
# Goal: Showcase how CSV can be used to open files and save files

# To use the csv reader and writer, we need to import that library
import csv

# Here is some data to save as CSV format
studentDataHeader = ["Student ID", "Last Name", "First Name", "Age", "Height", "GPA"]

studentData = [
    ["00001",       "Smith",        "Susan",        20,     6,          3.89],
    ["00002",       "Jones",        "Tommy",        18,     5.8,        3.64],
    ["00003",       "Lee",          "John",         26,     5.2,        2.95],
    ["00004",       "Hernadez",     "Melody",       22,     6.1,        4.00],
    ["00005",       "Anderson",     "Eva",          21,     5.4,        3.33],
    ["00006",       "Foster",       "Harper",       20,     5.9,        3.77],
    ["00007",       "Delacruz",     "Jaime",        19,     5.7,        3.95],
    ["00008",       "Newton",       "Duncan",       18,     6.3,        3.75],
    ["00009",       "Borman",       "Andrew",       100,    7.5,        4.00],
]

# This variable is set to a file type, it isa special data type that is an object
file = open("./data/new-student-data.csv", "w", newline='') # w is for write mode, newline='' removes spaces between lines

with file:

    # a writer is another special data type that is used for making csv's easier to write to
    writer = csv.writer(file)

    # most times, csv files have headers, so we can format a header as sow
    writer.writerow(studentDataHeader)

    # we can continue to write the data
    writer.writerows(studentData)

