#the data we need to retrieve
#1. the total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
# Import the datetime class from the datetime module.

import os
import csv


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object using the reader function
    file_reader = csv.reader(election_data)   
     # Print each row in the CSV file.
    for row in file_reader:
        print(row)  

# Close the file.
#election_data.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

