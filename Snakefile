rule all:
    input:
        "data/cleaned_state_data.csv",
        "visualizations/correlation_matrix.png",
        "visualizations/graduation_rate_vs_income.png",
        "visualizations/graduation_rate_by_race_gender.png",
        "visualizations/income_poverty_by_state.png",
        "visualizations/state_appropriations_by_grad_rank.png"

rule acquire_data:
    output:
        "data/socioeconomic_data.csv"
    shell:
        "python census_data_script.py"

rule clean_data:
    input:
        "data/socioeconomic_data.csv"
    output:
        "data/cleaned_state_data.csv"
    shell:
        "python data_cleaning.py"

rule create_visualizations:
    input:
        "data/cleaned_state_data.csv"
    output:
        "visualizations/correlation_matrix.png",
        "visualizations/graduation_rate_vs_income.png",
        "visualizations/graduation_rate_by_race_gender.png",
        "visualizations/income_poverty_by_state.png",
        "visualizations/state_appropriations_by_grad_rank.png"
    shell:
        "python data_cleaning.py"
