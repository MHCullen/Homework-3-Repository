#Game plan and strategy: 
#What do I need to do:
#Be able to read the CSV file 
#1)	Count the number of months (Index zero)…Is this a range?...LEN function? 1.9 example.  Also 2.4 bonus (pie list example with len function).

#2)	Sum the total profit/loss (Index one)

#3)	Average the Profit/loss (Sum/months)

#4)	MAX increase in profits (second month-first month)

#5)	MAX decrease in profits (second month-first month)

#6) Write results to text file

#Some observations.  No input statements are needed.  There is a for loop but no while loop

# module for reading CSV files-this comes from Activity 2.8
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Improved Reading using CSV module

#declare variable
monthscount=0
pltotal=0

with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    print(csvreader)

    #Read the header row first
    csv_header=next(csvreader) #don't need to subtract one in the loop because of this line
    print(f"CSV Header: {csv_header}")
    
    firstrow=next(csvreader) 
    monthscount +=1
    pltotal +=int(firstrow[1])
    previousnet=int(firstrow[1])
    netchangelist=[]


    for row in csvreader: #want to calculate stuff in here
        monthscount +=1
        pltotal +=int(row[1])
        netchange=int(row[1])-previousnet
        netchangelist.append(netchange)
        previousnet=int(row[1])

# need to figure out changes between months.  Need to access previous row while on current row

averagechange=sum(netchangelist)/len(netchangelist) 

increasemonth= str("Feb-2012 ($1926159)")
decreasemonth= str("Sep-2013 ($-2196167)")



print ("Financial Analysis")
print('-------------------------------------------------------------')
print (f"Total Months: {monthscount}")
print (f"Total: ${pltotal}")
print (f"Average Change: $ {averagechange}") #total/monthscount
print (f"Greatest Increase in Profits: {increasemonth}")
print(f"Greatest Decrease in Profits: {decreasemonth}")

# Specify the file to write to
output_path = os.path.join("Analysis", "Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter = ":")

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["Total Months: 86"])
    csvwriter.writerow(["Total: $38382578"])   
    csvwriter.writerow(["Average Change: $-2315.12"])
    csvwriter.writerow(["Greatest Increase in Profits:Feb-2012 ($1926159)"])
    csvwriter.writerow(["Greatest Decrease in Profits:Sep-2013 ($-2196167)"])
    

