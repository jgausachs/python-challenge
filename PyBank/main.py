# Import the necessary dependencies for os.path.join()
import os
import csv

# Function takes profit/loss for each period; returns the variance between periods
def deltas(list_elements):
    i = 0
    list_of_deltas = []
    for i in range(len(list_elements)-1):
        list_of_deltas.append(int(list_elements[i+1])-int(list_elements[i]))
    return (list_of_deltas)

# Function takes profit/loss for each period; returns average profit/loss
def delta_avg(list_elements):
    list_deltas = deltas(list_elements)
    length = len(list_deltas)
    total = 0.00
    for number in list_deltas:
        num_float = float(number)
        total += num_float
        average = total / length
        average_f = f"{average:.2f}"
    return average_f

# Function takes profit/loss for each period; returns the greatest increase 
def delta_max(list_elements):
    list_for_max = deltas(list_elements)
    max = -1000000
    index_max = 0
    for component in list_for_max:
        if component > max:
            max = component
            index_max = list_for_max.index(max) + 1
    return (index_max, max)

# Function takes profit/loss for each period; returns the greatest decrease 
def delta_min(list_elements):
    list_for_min = deltas(list_elements)
    min = 1000000
    index_min = 0
    for component in list_for_min:
        if component < min:
            min = component
            index_min = list_for_min.index(min) + 1
    return (index_min, min)

# Read file budget_data.csv
csvbudget = os.path.join("Resources", "budget_data.csv")

# Intial variables setting
profit_loss_date = []
profit_loss = []
cumul_profit = 0
dict_profit = {}
profit_max_tuple = ()
profit_max_mes = 0
profit_max_value = 0
profit_min_tuple = ()
profit_min_mes = 0
profit_min_value = 0
total_months = 0

# Open file budget_data.csv
with open(csvbudget, encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Set the loop to start past the header
    csvheader = next(csvfile)

    # Loop through the file counting the rows
    for row in csvreader:

        # Build list of profit/loss and associated periods
        profit_loss.append(row[1])
        profit_loss_date.append(row[0])

        # Add profit/loss over all periods on file
        cumul_profit += int(profit_loss[-1])

    # Create dictionary with period and profit/loss 
    for i in range(len(profit_loss_date)):
        dict_profit[profit_loss_date[i]]=profit_loss[i]

# Take function output; recast for use in print output
profit_max_tuple = delta_max(profit_loss)
profit_max_mes = profit_max_tuple[0]
profit_max_value = profit_max_tuple[1]
profit_min_tuple = delta_min(profit_loss)
profit_min_mes = profit_min_tuple[0]
profit_min_value = profit_min_tuple[1]
total_months = str(len(profit_loss))

# Display results on screen
print("\nFinancial Analysis")
print("-----------------------------")
print(f"Total Months: " + total_months)
print(f"Total: ${int(cumul_profit)}")
print(f"Average Change: ${delta_avg(profit_loss)}")
print(f"Greatest Increase in Profits: {profit_loss_date[profit_max_mes]} (${profit_max_value})")
print(f"Greatest Decrease in Profits: {profit_loss_date[profit_min_mes]} (${profit_min_value})\n")

# Build list to write to output file
output_to_file = [
    "Total Months", total_months,
    "Average Change", delta_avg(profit_loss),
    "Greatest Increase in Profits:", {profit_loss_date[profit_max_mes]}, {profit_max_value},
    "Greatest Decrease in Profits:", {profit_loss_date[profit_min_mes]}, {profit_min_value},
]

# Create path to output file
outputfile = os.path.join("analysis", "output.csv")

# Write data to file output.csv
with open(outputfile, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(output_to_file)

csvfile.close()