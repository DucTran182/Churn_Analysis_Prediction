import pandas as pd

# Load the user_info.txt file
users_info_df = pd.read_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\user_info.txt', sep='\t')

# Load the parsed log dataset
parsed_log_df = pd.read_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\parse_log.txt', sep='\t')

# Convert 'MAC' column to string in both DataFrames to ensure consistency
parsed_log_df['Mac'] = parsed_log_df['Mac'].astype(str)
users_info_df['Mac'] = users_info_df['Mac'].astype(str)

# Merge the datasets on the MAC column
combined_df = pd.merge(parsed_log_df, users_info_df, how='left', on='Mac')

# Save the combined dataset
combined_df.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\combined_log_analysis.txt', sep='\t', index=False)

print("Combined dataset saved to combined_log_analysis.txt")
