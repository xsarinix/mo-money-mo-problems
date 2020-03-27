# Import dependencies
import csv

# Declare variables
change_list = []
dates = []
values = []

# Read in CSV
import_path = 'budget_data.csv'
with open(import_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:
        dates.append(row[0])
        values.append(int(row[1]))
    
# Calculate total months in dataset
total_months = len(dates)

# Calculate net profit for company
total_profit = sum(values)

# Calculate average change from previous month and identify the greatest
# increase and decrease (date & amount) for entire period
for idx, (date, value) in enumerate(zip(dates[1:], values[1:])):
    change = value - values[idx]
    change_list.append(change)
    if change_list[idx] == max(change_list):
        greatest_increase = change
        increase_date = date
    if change_list[idx] == min(change_list):
        greatest_decrease = change
        decrease_date = date

average_change = sum(change_list) / len(change_list)

# Output - prints to terminal and exports as .txt file
output = (
    f'\nFinancial Analysis\n'
    f'---------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_profit:,.0f}\n'
    f'Average Change: ${average_change:,.2f}\n'
    f'Greatest Increase: {increase_date} (${greatest_increase:,.0f})\n'
    f'Greatest Decrease: {decrease_date} (${greatest_decrease:,.0f})\n'
)
print(output)

export_path = 'budget_analysis.txt'
with open(export_path, 'w') as txt_file:
    txt_file.write(output)