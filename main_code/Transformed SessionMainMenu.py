import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\combined_log_analysis.txt', sep='\t')

# Ensure 'SessionMainMenu' is treated as a string
df['SessionMainMenu'] = df['SessionMainMenu'].astype(str)

# Extract the timestamp part of 'SessionMainMenu'
df['Timestamp'] = df['SessionMainMenu'].str.split(':', n=1).str[1]

# Specify the datetime format based on the extracted timestamp
date_format = '%Y:%m:%d:%H:%M:%S:%f'

# Convert the extracted timestamp to datetime
df['SessionMainMenu'] = pd.to_datetime(df['Timestamp'], format=date_format, errors='coerce')

# Drop the intermediate 'Timestamp' column if no longer needed
df.drop(columns=['Timestamp'], inplace=True)

# Save the combined dataset
df.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\combined_log_analysis.txt', sep='\t', index=False)

# Verify the result
#print(df.head())
