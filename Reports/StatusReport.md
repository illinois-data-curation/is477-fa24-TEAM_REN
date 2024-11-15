# Status (Interim) Report



## Research Question(s): What is/are the question(s) you intend to address?

1. How do socioeconomic factors (e.g., income, poverty rates, employment) influence education outcomes (e.g., graduation rates, test scores) across different U.S. regions?
2. Are there regional patterns in how socioeconomic factors correlate with educational achievements, and what might these patterns indicate about resource allocation or policy needs?


## Timeline: 

### Week 1: Project Setup and Initial Data Acquisition

Evelina: Acquired the poverty and income data from the U.S. Census Bureau using an API key. The json data was converted into a csv file called socioeconomic_data.csv. The script for this acquisition is called census_data.py. The college completion dataset was acquired through Kaggle by downloading the zip file here: https://www.kaggle.com/datasets/thedevastator/boost-student-success-with-college-completion-da/discussion?sort=hotness. 

### Week 2: Data Cleaning and Initial Exploration

Natasha: Started integrating the datasets using Python and Pandas. Initial cleaning has involved handling missing values and ensuring consistent formatting across columns. Next, we will focus on merging datasets by common keys such as institution ID or state to prepare for analysis. Initial data profiling has been conducted to understand the distributions and detect any outliers. Summary statistics for key socioeconomic variables and graduation rates have been generated to inform further analysis.

### Week 3: Data Integration and Initial Analysis

Richa: In the process of setting up a Snakemake workflow to automate data cleaning, integration, and analysis. This will streamline reproducibility and ensure all steps can be executed seamlessly from raw data acquisition to final outputs. A primary challenge has been aligning data from different sources, particularly with variations in format and missing values. We have adjusted our integration approach to address these issues by standardizing column names for missing socioeconomic data where appropriate.

### Week 4: Final Analysis, Visualization, and Report Preparation

## Updated Timeline
- **Data Acquisition**: Completed
- **Data Cleaning and Integration**: In progress (to be completed by Nov 20)
- **Preliminary Analysis**: To begin after integration (target completion by Nov 25)
- **Workflow Automation with Snakemake**: In progress (to be completed by Nov 27)
- **Final Analysis and Visualization**: To start by Nov 28
- **Report Drafting and Documentation**: Begin Dec 1, to be completed by Dec 8
