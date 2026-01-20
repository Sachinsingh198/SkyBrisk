import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# SECTION 1: SETUP & THEMING
# ==========================================
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load a classic Data Science dataset (Iris or Tips)
df = sns.load_dataset('tips')

# ==========================================
# SECTION 2: HANDS-ON (Basic Visualization)
# ==========================================

def basic_plots(data):
    # 1. Histogram: Distribution of Total Bill
    plt.figure()
    sns.histplot(data['total_bill'], kde=True, color='blue')
    plt.title('Distribution of Total Bill')
    plt.savefig('distribution.png')
    plt.show()

# ==========================================
# SECTION 3: CLIENT PROJECT (Feature Dashboard)
# ==========================================

def create_feature_dashboard(data):
    """
    Creates a suite of plots to analyze relationships between features.
    """
    print("Generating Dashboard Plots...")

    # 1. Scatter Plot: Relationship between Bill and Tip
    plt.figure()
    sns.scatterplot(data=data, x='total_bill', y='tip', hue='day', style='time')
    plt.title('Bill Amount vs Tip Amount (By Day and Time)')
    plt.savefig('scatter_relationship.png')
    plt.show()

    # 2. Heatmap: Correlation Matrix
    plt.figure(figsize=(8, 6))
    # Note: Only calculate correlation for numeric columns
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Feature Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    plt.show()

    # 3. Pairplot: The "Big Picture"
    # This might take a few seconds as it plots every feature against every other
    print("Building Pairplot (this may take a moment)...")
    pair_plot = sns.pairplot(data, hue='sex', palette='husl')
    pair_plot.savefig('feature_pairplot.png')
    plt.show()

# --- EXECUTION ---
if __name__ == "__main__":
    # Run simple distribution check
    basic_plots(df)
    
    # Run the full project dashboard
    create_feature_dashboard(df)
    
    print("\n--- Project Complete ---")
    print("Files saved: distribution.png, scatter_relationship.png, correlation_heatmap.png, feature_pairplot.png")