# Your task is to create a Python script that analyses the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# Import dependencies

import os
import csv

#create empty lists to update the values from the csv file

Month_Counter = []
Change_in_profit_loss = []

#initialising PyBank variables

Months = 0
Change_in_profit_loss_counter = 0
Total_profit_loss = 0
Last_month_profit_loss = 0
This_month_profit_loss = 0

# Change directory to the directory of current python script

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Path to collect data from the Resources folder

file_csv = os.path.join('/Users/aliyazdan/Desktop/Data Analytics bootcamp /python-challenge/PyBank', 'Resources', 'budget_data.csv')


# Open and read in the CSV filE

with open(file_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first

    csv_header = next(csvfile)
             
    # Iterate through each row of data after the header

    for row in csv_reader:

        # Months counting

        Months += 1

        # Net total amount of "Profit/Losses" over the entire period

        This_month_profit_loss = int(row[1])
        Total_profit_loss += This_month_profit_loss

        if (Months == 1):

            # Change the value of previous month to the current month

            Last_month_profit_loss = This_month_profit_loss

            continue

        else:

            # Compute change in profit loss 

            Change_in_profit_loss_counter = This_month_profit_loss - Last_month_profit_loss

            # Append each month to the Month_Counter[]

            Month_Counter.append(row[0])

            # Append each Change_in_profit_loss_counter to the Change_in_profit_loss[]

            Change_in_profit_loss.append(Change_in_profit_loss_counter)

            # Make the This_month_profit_loss to be Last_month_profit_loss for the next loop

            Last_month_profit_loss = This_month_profit_loss

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes

    total_period_profit_loss = sum(Change_in_profit_loss)
    total_period_average_profit_loss = round(total_period_profit_loss/(Months - 1), 2)

    # Greatest increase and decrease in "Profit" over the entire period

    Greatest_increase = max(Change_in_profit_loss)
    Greatest_decrease = min(Change_in_profit_loss)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period

    Highest_month_index = Change_in_profit_loss.index(Greatest_increase)
    Lowest_month_index = Change_in_profit_loss.index(Greatest_decrease)

    # Locate the highest and lowest months

    Highest_month = Month_Counter[Highest_month_index]
    Lowest_month = Month_Counter[Lowest_month_index]

# In addition, your final script should both print the analysis to the terminal 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {Months}")
print(f"Total:  ${Total_profit_loss}")
print(f"Average Change:  ${total_period_average_profit_loss}")
print(f"Greatest Increase in Profits:  {Highest_month} (${Greatest_increase})")
print(f"Greatest Decrease in Losses:  {Lowest_month} (${Greatest_decrease})")


# and export a text file with the results.

PyBank_file = os.path.join("analysis", "analysis.txt")

with open(PyBank_file, "w") as analysis:

    analysis.write("Financial Analysis\n")
    analysis.write("----------------------------\n")
    analysis.write(f"Total Months:  {Months}\n")
    analysis.write(f"Total:  ${Total_profit_loss}\n")
    analysis.write(f"Average Change:  ${total_period_average_profit_loss}\n")
    analysis.write(f"Greatest Increase in Profits:  {Highest_month} (${Greatest_increase})\n")
    analysis.write(f"Greatest Decrease in Losses:  {Lowest_month} (${Greatest_decrease})\n")