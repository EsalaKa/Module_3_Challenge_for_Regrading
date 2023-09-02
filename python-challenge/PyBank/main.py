import csv
import os
# Open the CSV file with the path given,  csv.reader is used to read CSV file
with open(r'C:\Users\User\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # To count the rows, Initialize a variable because in the given dataset rows increments by month
    total_rows = 0

    # To count all the rows, total_rows variable increments by 1 so that all the rows in the CSV file is counted. 
    #In CSVfiles, rows are counted by 'for...in'
    for row in csv_reader:
        total_rows += 1

# As total rows contains the header, to exclude total_rows is reduced by 1. 
print("Financial Analysis")
print("-----------------------------------------")
print("Total Months:", total_rows-1)

# Open the CSV file using the same path as before.
with open(r'C:\Users\User\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # this variable is used to indicate what column in CSV file is focused because we need the column contans 'proft/loss' which is 1
    # (count as 0,1,..)
    target_column_index = 1  

    # This variable used keep the cumulative sum in previously chosen column and initializes it. 
    column_sum = 0

    # 'Try..Except' is used to handle the errors that might occur due to invalid value. Basically, we fix the column using target column
    #index, then iterates it using 'for..in' to get cumulative sum in our chosen column.
    for row in csv_reader:
        try:
            value = float(row[target_column_index])
            column_sum += value
        except (ValueError, IndexError):
            
            pass

# Print the sum of the column
print("Total: ${:.0f}".format(column_sum))

import csv
# By this definition, we define a function called 'average_and_max_differences() so that we aim to calculate the averange changes 
#and min and max profits that we will need in next steps
def average_and_max_differences(csv_file, column_index):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
  #This part is included to amend the code if necessary but could exclude the condition as we already know which column we need. 
  #This condition confirms that we are working with the data within calculable limit, for example column_index<0 is negetive which
  #should be ommited.   
        if column_index < 0 or column_index >= len(rows[0]):
            raise ValueError("Invalid column index")
   #create a list for 'differences'     
        differences = []
        
        for i in range(1, len(rows) - 1):                           # Start from the second row leaving the header row
            value1 = float(rows[i][column_index])                   #the current row of the chosen colun
            value2 = float(rows[i + 1][column_index])               # one after the current row of the column
            difference = (value2 - value1)                          # What we need to find
            differences.append(difference)                          #calculate differnces add to the list
        
        average_difference = sum(differences) / len(differences)    # Find the average
        max_difference = max(differences)                           # find max of average
        min_difference = min(differences)                           # Find min of  average
#max_difference is the maximum in the differences list. Find the index the differences list which gives the value. We add 2 because
# we dont include header row, and to exclude row counting differences in coding.
        max_row_index = differences.index(max_difference) +2
        min_row_index = differences.index(min_difference) +2

        max_other_value = (rows[max_row_index][other_column_index])
        min_other_value = (rows[min_row_index][other_column_index])
        
        return average_difference, max_difference, min_difference, max_other_value, min_other_value
#Definition finishes, then provide path, value and 
#
csv_file_path = r'C:\Users\User\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv'
column_index = 1  # Adjust this index to the desired column
other_column_index = 0  # Index of the column with corresponding values
average_diff, max_diff, min_diff, max_other_value, min_other_value = average_and_max_differences(csv_file_path, column_index)

print(f"Average Change: ${average_diff:.2f}")
print(f"Greatest Increase in Profits: {max_other_value} (${max_diff:.0f})")
print(f"Greatest Decrease in Profits: {min_other_value} (${min_diff:.0f})")

with open(r'C:\Users\User\OneDrive\Desktop\python-challenge\PyBank\analysis\Analysis.txt', 'w') as txt:
  txt.write("Financial Analysis\n")
  txt.write("-----------------------------------------\n")
  txt.write(f"Total Months: {total_rows-1}\n") 
  txt.write(f"Total: ${column_sum:.0f}\n")
#   txt.write(f"Total: ${{:.0f}.format(column_sum)}\n")
  txt.write(f"Average Change: ${average_diff:.2f}\n")
  txt.write(f"Greatest Increase in Profits: {max_other_value} (${max_diff:.0f})\n")
  txt.write(f"Greatest Decrease in Profits: {min_other_value} (${min_diff:.0f})\n")