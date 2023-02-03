import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

net_total_profit = 0
average_change = 0


date = []
profit = []

total_months = 0 


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])

        total_months = total_months + 1

        net_total_profit = net_total_profit + int(row[1])

        
    average_change = (net_total_profit / total_months)

    greatest_increase = max(profit)
    highest_index = profit.index(greatest_increase)
    highest_date = date[highest_index]

    greatest_decrease = min(profit)
    lowest_index = profit.index(greatest_decrease)
    lowest_date = date[lowest_index]

    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months)) 
    print("Total: $" + str(net_total_profit))
    print("Average Change: $" + str(round(float(average_change),2)))
    print("Greatest Increase in Profits: " + highest_date + " ($" + str(greatest_increase) + ")" )
    print("Greatest Decrease in Profits: " + lowest_date + " ($" + str(greatest_decrease) + ")" )


output_path = "budget_analysis.txt"

file =  open(output_path, 'w') 

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${net_total_profit} \n")
file.write(f"Average Change: ${round(float(average_change),2)}\n")
file.write(f"Greatest Increase in Profits: {highest_date} (${greatest_increase}) \n")
file.write(f"Dreatest Decrease in Profits: {lowest_date} (${ greatest_decrease})\n")