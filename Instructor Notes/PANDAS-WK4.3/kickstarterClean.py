# === kickStarterClean.ipynb ===
#%%
import pandas as pd


#%%
# The path to our CSV file
file = "Resources/KickstarterData.csv"

# Read our Kickstarter data into pandas
df = pd.read_csv(file)
df.head()


#%%
# Get a list of all of our columns for easy reference
df.columns


#%%
# Extract "name", "goal", "pledged", "state", "country", "staff_pick",
# "backers_count", and "spotlight"
reduced_kickstarter_df = df.loc[:, ["name", "goal", "pledged",
    "state", "country", "staff_pick", "backers_count", "spotlight"]]
reduced_kickstarter_df


#%%
# Remove projects that made no money at all
reduced_kickstarter_df = reduced_kickstarter_df.loc[(
    reduced_kickstarter_df["pledged"] > 0)]
reduced_kickstarter_df.head()


#%%
# Collect only those projects that were hosted in the US
hosted_in_us = reduced_kickstarter_df.loc[reduced_kickstarter_df["country"] == "US"]
hosted_in_us.head()


#%%
# Create a new column that finds the average amount pledged to a project
hosted_in_us["average_donation"] = hosted_in_us['pledged'] /
    hosted_in_us['backers_count']


#%%
# First convert "average_donation", "goal", and "pledged" columns to float
# Then Format to go to two decimal places, include a dollar sign, and use comma notation

hosted_in_us["average_donation"] = hosted_in_us["average_donation"].astype(float).map(
    "${:,.2f}".format)
hosted_in_us["goal"] = hosted_in_us["goal"].astype(float).map("${:,.2f}".format)
hosted_in_us["pledged"] = hosted_in_us["pledged"].astype(float).map("${:,.2f}".format)


#%%
hosted_in_us.head()


#%%
# Calculate the total number of backers for all US projects
hosted_in_us["backers_count"].sum()


#%%
# Calculate the average number of backers for all US projects
hosted_in_us["backers_count"].mean()


#%%
# Collect only those US campaigns that have been picked as a "Staff Pick"
picked_by_staff = hosted_in_us.loc[hosted_in_us["staff_pick"] == True]
picked_by_staff


#%%
# Group by the state of the campaigns and see if staff picks matter (Seems to matter quite a bit)
state_groups = picked_by_staff.groupby("state")
state_groups["name"].count()


