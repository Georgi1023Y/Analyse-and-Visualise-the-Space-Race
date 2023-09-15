# This is my Python Data Analysis project. I am analysing data from Space Race between the USA and the Soviet Union. This race started in 1957.
# Data that is saved in file called mission_launches.csv is from nextspaceflight.com

import pandas as pd
import matplotlib.pyplot as plt

# Load the data 
df_data = pd.read_csv('mission_launches.csv')

# # What is the shape of df_data?
# shape = df_data.shape
# # print("Shape of df_data:", shape)
# 
# # How many rows and columns does it have?
# num_rows, num_cols = shape
# 
# # What are the column names?
# column_names = df_data.columns.tolist()
# # print("Column names:", column_names)
# 
# # Are there any NaN values? - There is NaN values. 
# nan_values = df_data.isna().any().any()
# # print("Are there any NaN values?", nan_values)
# # Cleans the NaN values
# df_data_cleaned = df_data.dropna()
# 
# # Are there any duplicates?
# duplicates = df_data.duplicated().any()
# print("Are there any duplicates?", duplicates)
# 
# # Check for missing values
# missing_values = df_data.isna().sum()
# # print("Missing values in each column:")
# # print(missing_values)
# 
# # # Create a chart showing the number of space mission launched by organization
# # # Count the number of launches by each organization
# # launch_counts = df_data_cleaned['Organisation'].value_counts()
# # # Show the top 10 organizations:
# # top_10_launch_counts = launch_counts.head(10)
# # 
# # # Create a bar chart that shows 
# # plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# # top_10_launch_counts.plot(kind='bar', color='skyblue')
# # plt.title('Number of Space Mission Launches by Organization')
# # plt.xlabel('Organization')
# # plt.ylabel('Number of Launches')
# # plt.xticks(rotation=45)  # Rotate x-axis labels for readability
# # 
# # # Display the chart
# # plt.tight_layout()
# # plt.show()
# 
# # Count the number of active and retired rockets
# rocket_status_counts = df_data['Rocket_Status'].value_counts()
# # There are 790 active rockets and 3534 retired
# print(rocket_status_counts)
# 
# # Count the number of successful and failed missions
# mission_status_counts = df_data['Mission_Status'].value_counts()
# # There were 3879 missions ended with success and 339 with failiure
# print(mission_status_counts)
# 
# # How Expensive are the Launches? 
# # Drop rows with missing values in the 'Price' column
# df = df_data.dropna(subset=['Price'])
# 
# # Create a histogram of launch prices
# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
# 
# # Add labels and a title
# plt.xlabel('Launch Price')
# plt.ylabel('Frequency')
# plt.title('Distribution of Launch Prices')
# 
# # Show the histogram
# plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for better readability (optional)
# plt.tight_layout()
# plt.show()