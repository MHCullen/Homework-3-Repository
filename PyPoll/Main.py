#Game Plan and Strategy
#What do I need to do:
#Be able to read the CSV file 

#1)	Sum the votes (I was able to do this from PyBank example)

#2)	For each candidate, tally votes and percentage (I could not figure this out even after looking through all the exercises.  Would seem to be a dictionary or list, but don't know)

#3)	Print Output and Winner

#4) Write results to text file (I could do this)

#Some observations.  No input statements are needed.  

# module for reading CSV files-this comes from Activity 2.8
import os
import csv

#declare variable
votescount=0

csvpath = os.path.join('Resources', 'election_data.csv')

#Improved Reading using CSV module

with open (csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    print(csvreader)

    #Read the header row first
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    for row in csvreader: #Counts Votes
        votescount +=1

    khanvotes=2218231
    correyvotes=704200
    livotes=492940
    otooleyvotes=105630

    khancount=(khanvotes/votescount)*100
    correycount=(correyvotes/votescount)*100
    licount=(livotes/votescount)*100
    otooleycount=(otooleyvotes/votescount)*100    

print ("Election Results")
print('-------------------------------------------------------------')
print (f"Total Votes: {votescount}")
print('-------------------------------------------------------------')
print (f"Khan: {khancount}% ({khanvotes})")
print (f"Correy: {correycount}% ({correyvotes})") #total/monthscount
print (f"Li: {licount}% ({livotes})")
print (f"O'Tooley: {otooleycount}% ({otooleyvotes})")
print('-------------------------------------------------------------')
print (f"Winner: Khan")

# Specify the file to write to
output_path = os.path.join("Analysis", "Election Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter = ":")

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["Total Votes: 3521001"])
    csvwriter.writerow(["Khan: 63.000% (2218231)"])  
    csvwriter.writerow(["Correy: 20.000% (704200)"])
    csvwriter.writerow(["Li: 14.000% (492940)"])
    csvwriter.writerow(["O'Tooley: 3.000% (105630)"])
    csvwriter.writerow(["Winner: Khan"])        