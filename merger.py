import pandas as pd

# Read and store the csv files
file1 = pd.read_csv('data1.csv')
file2 = pd.read_csv('data2.csv')
file3 = pd.read_csv('data3.csv')
file4 = pd.read_csv('data4.csv')

# Merge the csv files based on the 'id' column
merged_data = file1.merge(file2, on='id', how='outer')
merged_data = merged_data.merge(file3, on='id', how='outer')
merged_data = merged_data.merge(file4, on='id', how='outer')

# Save the merged data to a new csv file

merged_data.dropna(inplace=True)
merged_data.to_csv('clean_merge.csv', index=False)

print(merged_data)
print('CSV files merged successfully.')
