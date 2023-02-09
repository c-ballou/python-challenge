#import modules for operating systems and csv files
import os
import csv

#bring in csv file
budget_data = os.path.join("Resources", "budget_data.csv")

#set variables
net_total_profit = 0
average_change = 0
date = []
profit = []
total_months = 0
profit_change = []

#set delimiter of the csv file and read the first row as a header
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #for loop to append the first column of csv to the date list
    #and the second column to the profit list
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
    
        #for loop adds to the total number of months and total profit
        total_months = total_months + 1
        net_total_profit = net_total_profit + int(row[1])

    #for loop to create list of changes in profit
    for i in range(85):
        profit_change.append(int(profit[i+1]) - int(profit[i]))

    average_change = (sum(profit_change) / (total_months - 1))

    greatest_increase = max(profit_change)
    highest_index = profit_change.index(greatest_increase)
    highest_date = date[highest_index + 1]

    greatest_decrease = min(profit_change)
    lowest_index = profit_change.index(greatest_decrease)
    lowest_date = date[lowest_index + 1]

    
#print results in terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months)) 
print("Total: $" + str(net_total_profit))
print("Average Change: $" + str(round(float(average_change),2)))
print("Greatest Increase in Profits: " + highest_date + " ($" + str(greatest_increase) + ")" )
print("Greatest Decrease in Profits: " + lowest_date + " ($" + str(greatest_decrease) + ")" )

#create text file with results
output_path = "budget_analysis.txt"

file =  open(output_path, 'w') 

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${net_total_profit} \n")
file.write(f"Average Change: ${round(float(average_change),2)}\n")
file.write(f"Greatest Increase in Profits: {highest_date} (${greatest_increase}) \n")
file.write(f"Dreatest Decrease in Profits: {lowest_date} (${ greatest_decrease})\n")