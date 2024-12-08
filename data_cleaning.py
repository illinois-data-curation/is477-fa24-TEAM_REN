import pandas as pd

state_sector_details = pd.read_csv('data/college_data/cc_state_sector_details.csv')
state_sector_grads = pd.read_csv('data/college_data/cc_state_sector_grads.csv')
socioeconomic_data = pd.read_csv('data/socioeconomic_data.csv')

state_merged = pd.merge(state_sector_details, state_sector_grads, on="stateid", how="inner")

socioeconomic_data.rename(columns={"State_Code": "stateid"}, inplace=True)

final_merged = pd.merge(state_merged, socioeconomic_data, on="stateid", how="inner")

relevant_columns = [
    'Median_Income', 'Poverty_Rate', 'grad_rate_rank', 
    'grad_100_rate', 'grad_150_rate', 'state_appr_value', 
    'state_appr_rank', 'gender', 'race', 'state_x'
]

final_cleaned = final_merged[relevant_columns]

final_cleaned.to_csv('data/cleaned_state_data.csv', index=False)

print(final_cleaned.head())
