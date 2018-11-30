import csv
import os

# Three lists each will be written to a column in csv file
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

# Zip all three lists together into tuples
roster = zip(indexes, employees, department)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row,
# and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

	# write column headers
    writer.writerow(["Index", "Employee", "Department"])

	# write all three lists to three columns at once
    writer.writerows(roster)

# # to print out to terminal:
# #comment out above code and run the code below
# for employee in roster:
#     print(employee)
