import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []

charles = 0
diana = 0
raymon = 0

charles_percent = 0
diana_percent = 0
raymon_percent = 0

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        candidates.append(row[2])
        if row[2] == "Charles Casper Stockham":
            charles = charles + 1
        if row[2] == "Diana DeGette":
            diana = diana + 1
        if row[2] == "Raymon Anthony Doane":
            raymon = raymon + 1

total_votes = len(candidates)

charles_percent = round((charles/total_votes)*100, 3)
diana_percent = round((diana/total_votes)*100, 3)
raymon_percent = round((raymon/total_votes)*100, 3)

most_votes = max(charles, diana, raymon)

if most_votes == charles:
    winner = "Charles Casper Stockham"
elif most_votes == diana:
    winner = "Diana DeGette"
else: 
    winner = "Raymon Anthony Doane"

#print results in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Charles Casper Stockham: " + (str(charles_percent)) + "% (" + str(charles) + ")")
print("Diana DeGette: " + (str(diana_percent)) + "% (" + str(diana) + ")")
print("Raymon Anthony Doane: " + (str(raymon_percent)) + "% (" + str(raymon) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

#create text file with results
output_path = "election_analysis.txt"
file =  open(output_path, 'w')

file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("-------------------------\n")
file.write(f"Charles Casper Stockham: {charles_percent}% ({charles})\n")
file.write(f"Diana DeGette: {diana_percent}% ({diana})\n")
file.write(f"Raymon Anthony Doane: {raymon_percent}% ({raymon})\n")
file.write("-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-------------------------\n")