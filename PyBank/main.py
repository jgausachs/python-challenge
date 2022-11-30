# Import the necessary dependencies for os.path.join()
import os
import csv

# Read the budget_data.csv file
csv_budget = os.path.join("Resources", "budget_data.csv" )

# Variable to track row count in csv_budget including header
rowCount = 0

# Open the .csv file
with open(csv_budget, encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through file counting the rows
    for rows in csvreader:
        rowCount += 1

print("Financial Analysis")
print("-----------------------------")

print("Total Months: " + str(rowCount - 1))  # Minus 1 to remove header
