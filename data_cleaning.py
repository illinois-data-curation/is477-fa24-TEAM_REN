# initial data cleaning

import pandas as pd

# reading each csv to create relevant data frames
state_sector_details = pd.read_csv('data/college_data/cc_state_sector_details.csv')
state_sector_grads = pd.read_csv('data/college_data/cc_state_sector_grads.csv')
socioeconomic_data = pd.read_csv('data/socioeconomic_data.csv')

# merging the data frames together
state_merged = pd.merge(state_sector_details, state_sector_grads, on="stateid", how="inner")

socioeconomic_data.rename(columns={"State_Code": "stateid"}, inplace=True)

final_merged = pd.merge(state_merged, socioeconomic_data, on="stateid", how="inner")

# selecting relevant columns needed for analysis (removing uneccessary columns)
relevant_columns = [
    'Median_Income', 'Poverty_Rate', 'grad_rate_rank', 
    'grad_100_rate', 'grad_150_rate', 'state_appr_value', 
    'state_appr_rank', 'gender', 'race', 'state_x'
]

final_cleaned = final_merged[relevant_columns]

final_cleaned.to_csv('data/cleaned_state_data.csv', index=False)

print(final_cleaned.head())


# data visualizations
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.makedirs('visualizations', exist_ok=True)


sns.set(style="whitegrid")

# correlation matrix

correlation_matrix = final_cleaned[['Median_Income', 'Poverty_Rate', 'grad_rate_rank', 
                                   'grad_100_rate', 'grad_150_rate', 'state_appr_value']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.tight_layout()

plt.savefig('visualizations/correlation_matrix.png')
plt.close()  

# graduation rates vs median income
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Median_Income', y='grad_rate_rank', data=final_cleaned, color='b')
plt.title('Graduation Rate Rank vs Median Income by State')
plt.xlabel('Median Income')
plt.ylabel('Graduation Rate Rank')

plt.savefig('visualizations/graduation_rate_vs_income.png')
plt.close()

# graduation rates related to race and gender - grouped bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x='race', y='grad_100_rate', hue='gender', data=final_cleaned, palette='muted')
plt.title('Graduation Rate (100%) by Race and Gender')
plt.xlabel('Race')
plt.ylabel('Graduation Rate (100%)')
plt.xticks(rotation=45)
plt.legend(title='Gender')

plt.savefig('visualizations/graduation_rate_by_race_gender.png')
plt.close()

# distribution of median income and poverty rate by state
fig, axes = plt.subplots(1, 2, figsize=(16, 6))


sns.barplot(x='state_x', y='Median_Income', data=final_cleaned, palette='Blues_d', ax=axes[0])
axes[0].set_title('Median Income by State')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=90)


sns.barplot(x='state_x', y='Poverty_Rate', data=final_cleaned, palette='Reds_d', ax=axes[1])
axes[1].set_title('Poverty Rate by State')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=90)

plt.tight_layout()

plt.savefig('visualizations/income_poverty_by_state.png')
plt.close()

# boxplot of state appropriations by graduation rate rank
plt.figure(figsize=(12, 6))
sns.boxplot(x='grad_rate_rank', y='state_appr_value', data=final_cleaned, palette='Set2')
plt.title('State Appropriations by Graduation Rate Rank')
plt.xlabel('Graduation Rate Rank')
plt.ylabel('State Appropriations Value')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('visualizations/state_appropriations_by_grad_rank.png')
plt.close()
