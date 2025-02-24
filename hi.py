import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("your_file.csv")  # Replace with actual file path

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Display column names
print("\nColumns in dataset:")
print(df.columns)

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Replace 'column_name' with the actual column name
column_name = "your_numeric_column"

# Calculate mean, median, and standard deviation
average_value = df[column_name].mean()
median_value = df[column_name].median()
std_dev = df[column_name].std()

print(f"\nAverage of {column_name}: {average_value}")
print(f"Median of {column_name}: {median_value}")
print(f"Standard Deviation of {column_name}: {std_dev}")

#data visualizations 
# Replace 'category_column' with actual categorical column
df['category_column'].value_counts().plot(kind='bar', color='skyblue')

plt.title("Category Distribution")
plt.xlabel("Categories")
plt.ylabel("Count")
plt.xticks(rotation=45)  # Rotate labels for readability
plt.show()

# Replace 'column_x' and 'column_y' with actual numerical columns
plt.scatter(df['column_x'], df['column_y'], color='red', alpha=0.5)

plt.xlabel("Column X")
plt.ylabel("Column Y")
plt.title("Scatter Plot of Column X vs Column Y")
plt.grid(True)
plt.show()

# Compute correlation matrix
correlation_matrix = df.corr()

# Plot heatmap manually using Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(correlation_matrix, cmap="coolwarm")

plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

# Add colorbar
fig.colorbar(cax)

plt.title("Correlation Heatmap")
plt.show()