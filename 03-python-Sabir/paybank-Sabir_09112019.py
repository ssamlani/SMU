
# Import modules os and csv
import os
import csv

# Set the path for the CSV file in PyBankcsv and the Output text  file 
mypath =r"C:\Users\ssamlani\OneDrive\VSC_Doc\03_Python_Sabir\budget_data.csv"
mypath2 =r"C:\Users\ssamlani\OneDrive\VSC_Doc\03_Python_Sabir\PyBank_FinAnlz_Output_Sabir.txt"

PyBankcsv = os.path.join(mypath)
Finance_txt = os.path.join(mypath2)

# Create  lists to store data. 
profit = []
monthly_changes = []
date = []

# Initialize the variables 
count = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0

# Open the CSV using the set path 

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop trough each row 
    for row in csvreader:    
      # Use count to count the number of months in this dataset
      count = count + 1 

      # Will use it to collect the greatest increase and decrease in profit
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profit from month to month. Then calculate the average change in profit
      final_profit = int(row[1])
      monthly_change_profit = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profit)

      total_change_profit = total_change_profit + monthly_change_profit
      initial_profit = final_profit

      #Calculate the average change in profit
      average_change_profit = (total_change_profit/count)
      
      #Find the max and min change in profit and the corresponding dates these changes 
      greatest_increase_profit = max(monthly_changes)
      greatest_decrease_profit = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profit)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profit)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total : " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profit)))
    print("Greatest Increase in profit: " + str(increase_date) + " ($" + str(greatest_increase_profit) + ")")
    print("Greatest Decrease in profit: " + str(decrease_date) + " ($" + str(greatest_decrease_profit)+ ")")
    print("----------------------------------------------------------")
# Write results to test file 
with open(Finance_txt, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total profit: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profit)) + "\n")
    text.write("    Greatest Increase in profit: " + str(increase_date) + " ($" + str(greatest_increase_profit) + ")\n")
    text.write("    Greatest Decrease in profit: " + str(decrease_date) + " ($" + str(greatest_decrease_profit) + ")\n")
    text.write("----------------------------------------------------------\n")

