# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# the forward slashes are added by the .join() function
csvpath = os.path.join('Resources', 'accounting.csv')

print(csvpath)  #verify if path is correctly built

# # Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler:
    #----------------------------
    #  lines are strings returned
    #  by regular file reader
    #----------------------------
    lines = file_handler.read()
    print(lines)
    print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    # output <_csv.reader object at 0x10b40bf98>

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    # Read each row of data after the header
    for row in csvreader:
        #----------------------------
        #  lines are lists returned
        #  by csv reader
        #----------------------------
        print(row)
