"""
Week 2 Submission: Data Structures, Functions, and Data Cleaning
Name: Sachin Singh
Date: January 2026
"""

# ==========================================
# SECTION 1: HANDS-ON (Data Transformations)
# ==========================================

def sum_of_squares(numbers):
    """Calculates the sum of squares: \sum x_i^2"""
    return sum([x**2 for x in numbers])

def filter_high_values(data, threshold):
    """Filters a list to return only values above a threshold."""
    return [item for item in data if item > threshold]

# Lambda version for quick filtering (even vs odd)
is_even = lambda x: x % 2 == 0

# Recursion example: Factorial
def get_factorial(n):
    if n <= 1: return 1
    else: return n * get_factorial(n-1)


# ==========================================
# SECTION 2: CLIENT PROJECT (Data Cleaning)
# ==========================================

def clean_client_data(raw_data):
    """
    Cleans a list of records by:
    1. Removing duplicates (using sets)
    2. Removing null/empty values
    3. Normalizing text (lowercase & stripped)
    """
    # Remove exact duplicates by converting to set, then back to list
    unique_data = list(set(raw_data))
    
    # Filter out empty strings or None values and normalize
    cleaned_data = [item.strip().lower() for item in unique_data if item]
    
    return sorted(cleaned_data)

# --- EXECUTION ---
if __name__ == "__main__":
    # Test Hands-on
    nums = [1, 2, 3, 4, 5]
    print(f"Sum of Squares: {sum_of_squares(nums)}")  # Output: 55
    print(f"Factorial of 5: {get_factorial(5)}")      # Output: 120

    # Test Client Project
    dirty_data = [" Apple", "banana", "APPLE", "  ", "Orange", "banana", None]
    final_data = clean_client_data(dirty_data)
    
    print("\n--- Client Project Results ---")
    print(f"Original Count: {len(dirty_data)}")
    print(f"Cleaned Data: {final_data}")
    print(f"Final Count: {len(final_data)}")