#Create a proxy churn label based on the number of service interactions, 
#A user is considered churned if their interaction frequency lower that the average of interactions (lower than 9).
import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\user_retention.txt', sep='\t')

# Assume there's a column 'ServiceUsageCount' that holds the interaction count
average_interactions = df['InteractionCount'].mean()

# Define the churn threshold as one-third of the maximum interactions
churn_threshold = average_interactions 

# Create a new column for churn labels
df['churn_label'] = df['InteractionCount'].apply(lambda x: 1 if x <= churn_threshold else 0)

# Check the distribution of churn labels
print(df['churn_label'].value_counts())

# Save the labeled data
df.to_csv(r'C:\Users\james\OneDrive\Desktop\DataSampleTest\churn_labeled_data.txt', sep='\t', index=False)
