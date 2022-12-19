# Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# Import dependencies

import os
import csv


#create empty lists to update the values from the csv file

# List for candidates 
Candidates = []
# List for votes for each of the candidates
Candidates_votes = []
# Votes Counter
votes_counter = 0

# Change directory to the directory of current python script

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Path to collect data from the Resources folder

file_csv = os.path.join('/Users/aliyazdan/Desktop/Data Analytics bootcamp /python-challenge/PyPoll', 'Resources', 'election_data.csv')

# Open and read in the CSV filE

with open(file_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first

    csv_header = next(csvfile)


 # Iterate through each row of data after the header

    for row in csv_reader:

        #Counting the votes - The total number of votes cast
        votes_counter += 1

        #A complete list of candidates who received votes
        #The total number of votes each candidate won
        #Adding name of the new candidates with a vote to the empty list and then adding 1 vote under candidate's name 

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Candidates_votes.append(1)

        #if name of the new candidates with a vote already exists in the empty list then only adding 1 vote under candidate's name, identified by their index    
        else:
            index = Candidates.index(row[2])
            Candidates_votes [index] += 1
    
    # The winner of the election based on popular vote

    #  Finding the highest number of votes amongst the candidates

    Winner_election = max(Candidates_votes)

    # Finding the index for the candidate with the highest number of votes 

    index = Candidates_votes.index(Winner_election)

    # Name of the winning candidate from the candidates list based on the winner index

    Winner_candidate = Candidates[index]

    # In addition, your final script should both print the analysis to the terminal 

print("Election Results")
print("----------------------------")
print(f"Total Votes:  {str(votes_counter)}")
print("----------------------------")

    # The percentage of votes each candidate won
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(round((Candidates_votes[i]/votes_counter) * 100,3))}% ({str(Candidates_votes[i])})")
print("----------------------------")
print(f"Winner: {Winner_candidate}")
print("----------------------------")

# and export a text file with the results.

PyPoll_file = os.path.join("analysis", "analysis.txt")

with open(PyPoll_file, "w") as analysis:

    analysis.write("Election Results\n")
    analysis.write("----------------------------\n")
    analysis.write(f"Total Votes:  {str(votes_counter)}\n")
    analysis.write("----------------------------\n")
    for i in range(len(Candidates)):
     analysis.write(f"{Candidates[i]}: {str(round((Candidates_votes[i]/votes_counter) * 100,3))}% ({str(Candidates_votes[i])})\n")
    analysis.write("----------------------------\n")
    analysis.write(f"Winner: {Winner_candidate}\n")
    analysis.write("----------------------------\n")