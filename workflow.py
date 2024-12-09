import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_data_cleaning():
    """Run the data_cleaning.py script."""
    print("Running data cleaning...")
    subprocess.run(["python", "Reports/data_cleaning/data_cleaning.py"], check=True)

def generate_visualizations():
    """Generate visualizations using the cleaned data."""
    print("Generating visualizations...")
    # Load the cleaned data
    cleaned_data = pd.read_csv('data/cleaned_state_data.csv')
    
    # Select only numeric columns for correlation
    numeric_data = cleaned_data.select_dtypes(include=["number"])
    
    # Visualization 1: Correlation Matrix
    correlation = numeric_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.savefig('visualizations/correlation_matrix.png')
    plt.close()

    # Visualization 2: Graduation Rates by Poverty Rate
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=cleaned_data, 
        x="Poverty_Rate", 
        y="grad_150_rate", 
        hue="state_x",  # Non-numeric column can still be used as a category for hue
        palette="viridis", 
        size="Median_Income", 
        sizes=(20, 200)
    )
    plt.title("Graduation Rates vs Poverty Rate by State")
    plt.xlabel("Poverty Rate")
    plt.ylabel("Graduation Rate (150%)")
    plt.legend(title="States", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.savefig('visualizations/graduation_rate_vs_poverty.png')
    plt.close()

    print("Visualizations saved to the visualizations/ directory.")

def main():
    # Step 1: Run data cleaning script
    run_data_cleaning()
    
    # Step 2: Generate visualizations
    generate_visualizations()

if __name__ == "__main__":
    main()
