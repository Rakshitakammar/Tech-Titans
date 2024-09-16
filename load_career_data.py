import pandas as pd
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Construct the absolute path to the Excel file
file_path = 'C:/Users/raksh/Desktop/SIH/expanded_career_data.csv.xlsx'

# Load the career dataset from the Excel file
try:
    career_df = pd.read_excel(file_path)
    # Display all rows of the DataFrame
    print("Complete dataset:")
    print(career_df.to_string())  # This prints the entire dataset
except FileNotFoundError as e:
    print(f"Error: {e}")
except ImportError as e:
    print(f"Import Error: {e}")
