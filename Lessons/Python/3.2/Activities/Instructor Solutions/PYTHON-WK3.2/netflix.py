# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("Resources", "netflix_ratings.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
    	# ------------------------------------------------------
    	# converting to lower case is not needed but provides
    	# greater robustness to program (more chance to find a
    	# movie) regardless of how to user enter the movies name
    	# ------------------------------------------------------
        if row[0].lower() == video.lower():
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
            found = True

            # BONUS: Stop at first results to avoid duplicates
            break	# exit loop before all rows are read
        #else:
        	#print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

    # If the video is never found, alert the user
    # multiple ways to check found status
    #if found == False:
    #if found is False:
    if not found:
        print("Sorry about this, we don't seem to have what you are looking for!")
