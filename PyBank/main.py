# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os 
print(os.getcwd())

# Files to load and output (update with correct file paths)
file_to_load = "C:/Users/khati/OneDrive/Desktop/03-Python/python-challenge/PyBank/Resources/budget_data.csv"  # Input file path
file_to_output = os.path.join("C:/Users/khati/OneDrive/Desktop/03-Python/python-challenge/PyBank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Process each row of data
    for row in reader:

    # Track the total
        total_months += 1
        total_net += int(row[1])

    # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])

    # Calculate the greatest increase in profits (month and amount)
        net_change_list += [net_change]
        month_of_change += [row[0]]

    # Calculate the greatest decrease in losses (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change across the months
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
# Generate the output summary
    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
    print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
