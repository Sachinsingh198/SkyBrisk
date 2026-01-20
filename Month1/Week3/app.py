import numpy as np
import pandas as pd

# ==========================================
# SECTION 1: NUMPY HANDS-ON
# ==========================================

# Create a 3x3 array of numbers 1-9
array_2d = np.arange(1, 10).reshape(3, 3)

# Broadcasting: Add 10 to every element without a loop
plus_ten = array_2d + 10

# Calculate column-wise mean
col_mean = np.mean(array_2d, axis=0)


# ==========================================
# SECTION 2: CLIENT PROJECT (Pandas Data Manipulation)
# ==========================================

# 1. Create a sample "dirty" dataset
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'David', 'Charlie'],
    'Department': ['Sales', 'IT', 'Sales', 'Sales', 'IT', 'HR', 'Sales'],
    'Salary': [50000, 60000, 55000, 50000, np.nan, 45000, 55000],
    'Bonus': [2000, 3000, np.nan, 2000, 1500, 1000, 2500]
}

df = pd.DataFrame(data)

def process_payroll_data(df):
    """
    Cleans and aggregates the dataset.
    """
    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Handle missing values: 
    # Fill Salary with the median, Fill Bonus with 0
    df['Salary'] = df['Salary'].fillna(df['Salary'].median())
    df['Bonus'] = df['Bonus'].fillna(0)

    # Add a calculated column (Total Pay)
    df['Total_Pay'] = df['Salary'] + df['Bonus']

    # Grouping: Calculate average Total Pay per Department
    summary = df.groupby('Department')['Total_Pay'].mean().reset_index()
    
    return df, summary

# --- EXECUTION ---
if __name__ == "__main__":
    cleaned_df, dept_summary = process_payroll_data(df)

    print("--- Cleaned Dataset ---")
    print(cleaned_df)
    
    print("\n--- Department Average Salary Summary ---")
    print(dept_summary)