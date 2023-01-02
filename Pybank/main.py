import csv
import os
filepath = os.path.join("Resources","budget_data.csv") 
output_path = os.path.join("analysis","budgetanalysis.txt")

#Defined everything
months = 0 
total_change = 0
monthlists = []
netchange = []
maxincrease = ["",0]
maxdecrease = ["", 9999999999]

#Read in the Data

with open(filepath) as file:
    reader = csv.reader(file)
    header = next(reader)
    firstrow = next(reader)
    months += 1 
    total_change +=int(firstrow[1])
    previouschange = int(firstrow[1])
    for row in reader:
        months += 1 
        total_change += int(row[1])
        delta = int(row[1]) - previouschange
        previouschange = int(row[1])
        netchange.append(delta)
        # same as above:
        # netchange +=[delta]
        monthlists .append(row[0])

        if delta > maxincrease[1]:
            maxincrease[1] = delta
            maxincrease[0] = row[0]
        if delta < maxdecrease[1]:
            maxdecrease[1] = delta
            maxdecrease[0] = row[0]

monthlyavgdelta = sum(netchange) / len(netchange)

output=(f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total_change:,.2f}
Average Change: ${monthlyavgdelta:,.2f}
Greatest Increase in Profits: {maxincrease[0]} (${maxincrease[1]:,.2f})
Greatest Decrease in Profits: {maxdecrease[0]} (${maxdecrease[1]:,.2f})
""")

print(output)

with open(output_path,"w") as file:
    file.write(output)
