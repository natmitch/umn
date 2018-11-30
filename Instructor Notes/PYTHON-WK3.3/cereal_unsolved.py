
"""
# Instructions
* Open the file, `cereal.csv` and start by skipping the header row. See hints below for this.
* Read through the remaining rows and find the cereals that contain five grams of fiber or more, printing the data from those rows to the terminal.
## Hint
   * Everything within the csv is stored as a string and certain rows have a decimal.
     This means that they will have to be cast to be used.
   * The csv.Reader begins reading the csv file at the first row.
     `next(csv_reader, None)` will skip the header row.
     Refer to this stackoverflow answer on [how to skip the header]
        (https://stackoverflow.com/a/14257599) for more information.
   * Integers in Python are whole numbers and, as such,
     cannot contain decimals. As such, your numbers containing decimal points
     will have to be cast as a `float.
## Bonus
   * Try the following again but this time using `cereal_bonus.csv`, which does not include a header.
"""
# include helper library(ies) - dependencies 
import os
import csv

# add items for my prog
cereal_csv = os.path.join("../Resources", "cereal.csv")

# open the csv file
with open(cereal_csv, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ",")

  # create a csv reader
  csv_header = next(csvfile)

  # print the header
  print(f"Header: {csv_header}")

  # loop thru csv file
  for row in csvreader:
    
    # to find cereal that are >= 5 gr of fibers
    if float(row[7]) >= 5:
      # if found print row
      print(row)
