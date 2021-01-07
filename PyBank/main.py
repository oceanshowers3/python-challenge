#Python script that calculates each of the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

#import everything we need to get started
import csv
import os
import sys

#set up the file path
budgetDataCSV = os.path.join("Resources", "budget_data.csv")

#variable list
numMonths = 0 
netTotal = 0
change = 0
netChange = []
avgChange = 0
maxChange = 0
minChange = 0
maxChangeDate = 0
minChangeDate = 0
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]
originalStdout = sys.stdout

#open the budget_data CSV file
with open(budgetDataCSV) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    #Account for header
    header = next(csvReader)
    firstRow = next(csvReader)
    numMonths += 1
    netTotal += int(firstRow[1])
    prevNet = int(firstRow[1])

    #for each month in the CSV file:
    for month in csvReader:
        #count number of months
        numMonths = numMonths + 1
        #count total profit/losses
        netTotal = netTotal + int(month[1]) 
        #calculate the changes between months
        change = int(month[1]) - prevNet 
        prevNet = int(month[1])
        netChange += [change]
        #average the changes between months
        avgChange = sum(netChange)/len(netChange)
        #find the greatest increase in profits
        if change > greatestIncrease[1]:
            greatestIncrease[0] = month[0]
            greatestIncrease[1] = change
        #find the greatest decrease in losses
        if change < greatestDecrease[1]:
            greatestDecrease[0] = month[0]
            greatestDecrease[1] = change

    #print results
    print("Months: ", (numMonths))
    print("Net Total: $", (netTotal))
    print("Average Changes: $", avgChange)
    print("Greatest Increase in Profits: ", greatestIncrease[0], " $", greatestIncrease[1])
    print("Greatest Decrease in Losses: ", greatestDecrease[0], " $", greatestDecrease[1])

    #print results to txt file
    with open('output.txt', 'a+') as f:
        sys.stdout = f 
        print("Months: ", (numMonths))
        print("Net Total: $", (netTotal))
        print("Average Changes: $", avgChange)
        print("Greatest Increase in Profits: ", greatestIncrease[0], " $", greatestIncrease[1])
        print("Greatest Decrease in Losses: ", greatestDecrease[0], " $", greatestDecrease[1])
        sys.stdout = originalStdout 