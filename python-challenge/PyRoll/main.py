import csv
import os
# Function defines
def count_items_column(csv_file, column_index):            # Opens CSV file and reads 
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)                      # Creates CSV reader object csv_reader 
        next(csv_reader)                                   # Leave the header row
        count = 0                                          # Initialises count
        
        for row in csv_reader:
            if column_index < len(row):
                count += 1                                # Increment the count for each item in the specified column
        
        return count

# Gives file path
file_path = r'C:\Users\User\OneDrive\Desktop\python-challenge\PyRoll\Resources\election_data.csv'
column_index = 2                                          # Adjust this index to the desired column
item_count = count_items_column(file_path, column_index)
print("Election Results")
print("--------------------------")
print(f"Total Votes: {item_count}")
print("--------------------------")

file_path = r"C:\Users\User\OneDrive\Desktop\python-challenge\PyRoll\Resources\election_data.csv"

# Initialize variables to store data
data = []
header = None

with open(file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Read the header row
    header = next(csv_reader, None)
    
    # Read the rest of the rows
    for row in csv_reader:
        data.append(row)

# Column index where the items of interest are located
column_index = 2  # Adjust this index based on your CSV file

item_to_count_1 = "Charles Casper Stockham"                  # Replace with the item you want to count
item_to_count_2 = "Diana DeGette"                            # Replace with the item you want to count
item_to_count_3 = "Raymon Anthony Doane"

count_1 = 0
count_2 = 0
count_3 = 0

# Count occurrences
for row in data:
    if row[column_index] == item_to_count_1:
        count_1 += 1
    if row[column_index] == item_to_count_2:
        count_2 += 1
    if row[column_index] == item_to_count_3:
        count_3 += 1

# Calculate percentages
percentage_1 = (count_1 / item_count) * 100
percentage_2 = (count_2 / item_count) * 100
percentage_3 = (count_3 / item_count) * 100

# Create a dictionary to store the counts
item_counts = {
    item_to_count_1: count_1,
    item_to_count_2: count_2,
    item_to_count_3: count_3
}

# Find and print the item with the maximum count
max_item = max(item_counts, key=item_counts.get)
max_count = item_counts[max_item]  

# Print individual item counts and percentages
print(f"{item_to_count_1}: {percentage_1:.3f}% ({count_1})")
print(f"{item_to_count_2}: {percentage_2:.3f}% ({count_2})")
print(f"{item_to_count_3}: {percentage_3:.3f}% ({count_3})")

print("--------------------------")
print(f"Winner: {max_item} ")
print("--------------------------")

with open(r'C:\Users\User\OneDrive\Desktop\python-challenge\PyRoll\analysis\Analysis.txt', 'w') as txt:

   txt.write("Election Results\n")
   txt.write("--------------------------\n")
   txt.write(f"Total Votes: {item_count}\n")
   txt.write("--------------------------\n") 
   txt.write(f"{item_to_count_1}: {percentage_1:.3f}% ({count_1})\n")
   txt.write(f"{item_to_count_2}: {percentage_2:.3f}% ({count_2})\n")
   txt.write(f"{item_to_count_3}: {percentage_3:.3f}% ({count_3})\n")

   txt.write("--------------------------\n")
   txt.write(f"Winner: {max_item} \n")
   txt.write("--------------------------\n") 


 