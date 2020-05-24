import os
import csv

csvpath = "Resources/election_data.csv"

Candidate_list=[]
Candidate_votes=[]
total_votes=0

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:
        #The total number of votes cast
        total_votes += 1
        # #A complete list of candidates who received votes
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])

        #The percentage of votes each candidate won

        #The total number of votes each candidate won

        # The winner of the election based on popular vote.

print(f"Election Results")
print("Total Votes:"+(str(len(Candidate_votes))))
print(str(Candidate_list))

#line3=("Total:"+(str(Total)))
#line4=("Average change:"+(str(Average)))
#line5=("Greatest increase in profits:"+(str(Month[Increase.index(max(Increase))+1]))+(str(max(Increase))))
#line6=("Greatest decrease in profits:"+(str(Month[Increase.index(min(Increase))+1]))+(str(min(Increase))))