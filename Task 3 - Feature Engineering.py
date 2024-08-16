import pandas as pd

# Load the combined dataset
combined_df = pd.read_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\combined_log_analysis.txt', sep='\t')

# 1. Service Usage Frequency: Count interactions per user
service_usage_freq = combined_df.groupby('Mac').size().reset_index(name='ServiceUsageCount')

# 2. Duration Analysis: Total time spent using services by each user
duration_analysis = combined_df.groupby('Mac')['RealTimePlaying'].sum().reset_index(name='TotalTimeSpent')

# 3. Top Content Watched: Identify the most popular content
top_content_watched = combined_df.groupby('ItemID').size().reset_index(name='WatchCount').sort_values(by='WatchCount', ascending=False)

# 4. User Engagement by App: Determine engagement by AppName
user_engagement_by_app = combined_df.groupby('AppName').size().reset_index(name='EngagementCount').sort_values(by='EngagementCount', ascending=False)

# 5. User Retention: Analyze user activity over time (you might need a timestamp for this)
# For simplicity, let's count interactions per user (retention over MAC)
user_retention = combined_df.groupby(['Mac', 'SessionMainMenu']).size().reset_index(name='InteractionCount')

# 6. Time-of-Day Analysis: Determine when users are most active
# Assuming 'SessionMainMenu' is a timestamp, extract hour and analyze
combined_df['HourOfDay'] = pd.to_datetime(combined_df['SessionMainMenu']).dt.hour
time_of_day_analysis = combined_df.groupby('HourOfDay').size().reset_index(name='ActivityCount').sort_values(by='ActivityCount', ascending=False)

# Save the results to different files
service_usage_freq.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\service_usage_frequency.txt', sep='\t', index=False)
duration_analysis.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\duration_analysis.txt', sep='\t', index=False)
top_content_watched.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\top_content_watched.txt', sep='\t', index=False)
user_engagement_by_app.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\user_engagement_by_app.txt', sep='\t', index=False)
user_retention.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\user_retention.txt', sep='\t', index=False)
time_of_day_analysis.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\time_of_day_analysis.txt', sep='\t', index=False)

print("All analyses have been saved successfully.")
