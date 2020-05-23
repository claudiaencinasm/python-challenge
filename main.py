import os
import csv

csvpath = "Resources/budget_data.csv"

#lists to store data
Month = []
Profit=[]
Increase=[]

Total=0

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # Read through each row of data 
    for row in csvreader:
        #The total number of months included in the dataset
        Month.append(row[0])
        #The net total amount of “Profit/Losses” over the entire period
        Total += int(row[1])
        #The greatest increase in profits (date and amount) over the entire period
        Profit.append(int(row[1]))
    for i in range((len(Profit))-1):
        Increase.append(Profit[i + 1] - Profit[i])

#The average of the changes in “Profit/Losses” over the entire period      
Average= int(sum(Increase)) / (len(Month))



line1=(f"Financial Analysis")
line2=("Total Months:"+(str(len(Month))))
line3=("Total:"+(str(Total)))
line4=("Average change:"+(str(Average)))
line5=("Greatest increase in profits:"+(str(Month[Increase.index(max(Increase))+1]))+(str(max(Increase))))
line6=("Greatest decrease in profits:"+(str(Month[Increase.index(min(Increase))+1]))+(str(min(Increase))))

output=(line1,line2,line3,line4,line5,line6)
print(output)

file=open("budget_data.txt","w")
file.write(str(output))
file.close()
