# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import string
# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

totalMonths = 0 
total = 0.00
totalChange = 0.00
averageChange = 0.00
greatestIncrease = 0.00
greatestDecrease = 0.00
greatestIncreaseMonth = ""
greatestDecreaseMonth = ""

lastRow = 0.00
rowCount = 1

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        totalMonths += 1
        total += float(row[1])
        if (rowCount > 1):
            totalChange = lastRow - float(row[1]) 
        rowCount += 1
        lastRow = float(row[1])
 
        if (lastRow > greatestIncrease):
            greatestIncrease = lastRow
            greatestIncreaseMonth = row[0] 
               
        if (lastRow < greatestDecrease): 
            greatestDecrease = lastRow
            greatestDecreaseMonth = row[0]     

averageChange = float(totalChange)/float(rowCount)

result = "    Financial Analysis \n" \
"----------------------------\n" \
"Total Months: " + str(totalMonths) + \
"\nTotal: " + "${:0,.2f}".format(total).replace('$-','-$') +\
"\nAverage  Change: " + "${:0,.2f}".format(averageChange).replace('$-','-$') + \
"\nGreatest Increase in Profits: " + greatestIncreaseMonth  + " ${:0,.2f}".format(greatestIncrease).replace('$-','-$') + \
"\nGreatest Decrease in Profits: " + greatestDecreaseMonth + " ${:0,.2f}".format(greatestDecrease).replace('$-','-$') 

print(result)