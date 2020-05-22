import os
import csv

csvpath = "C:/Users/Encinas/Desktop/DATAVIZ/python/pybank/Resources/budget_data.csv"

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

print("Financial Analysis")
print(f"Total Months:"+(str(len(Month))))
print(f"Total: {str(Total)}")
print(f"Average change: {str(Average)}")
print(f"Greatest increase in profits:{str(Month[Increase.index(max(Increase))+1])} {str(max(Increase))}")
print(f"Greatest decrease in profits:{str(Month[Increase.index(min(Increase))+1])} {str(min(Increase))}")

# Zip lists together
#cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
file=open("budget_data.txt","w")

file.write("Financial analysis")
file.close()

#output_file = os.path.join("budget_data.txt")

#with open("budget_data.txt", "r") as file:
    #print("Financial Analysis")
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left","Percent of Reviews", "Length of Course"])
    # Write in zipped rows
    #writer.writerows(cleaned_csv)
