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

Candidates = []
Candidates_votes = []

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

        Candidates.append(row[2])
