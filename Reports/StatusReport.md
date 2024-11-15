# Status (Interim) Report



## Research Question(s): What is/are the question(s) you intend to address?

1. How do socioeconomic factors (e.g., income, poverty rates, employment) influence education outcomes (e.g., graduation rates, test scores) across different U.S. regions?
2. Are there regional patterns in how socioeconomic factors correlate with educational achievements, and what might these patterns indicate about resource allocation or policy needs?


## Timeline: 

### Week 1: Project Setup and Initial Data Acquisition

Evelina's tasks: Acquired the poverty and income data from the U.S. Census Bureau using an API key. The json data was converted into a csv file called socioeconomic_data.csv. The script for this acquisition is called census_data.py. The college completion dataset was acquired through Kaggle by downloading the zip file here: https://www.kaggle.com/datasets/thedevastator/boost-student-success-with-college-completion-da/discussion?sort=hotness. 

Specific relevance to project setup: The initial data acquisition will help us start to complete some of the preliminary cleaning and analysis that will take place in the upcoming weeks. Additional data maybe needed however the acquisition of these two datasets is instrumental in starting our initial analysis. The initial analysis will start off by examining various socioeconomic factors listed in the data sets (e.g., income, poverty rates, employment) as well as various demographics (regions, ages, gender, etc.) to better understand the patterns between demographics and socioeconomic standings. 

### Week 2: Data Cleaning and Initial Exploration

Richa's tasks: Started integrating the datasets using Python and Pandas. Initial cleaning has involved handling missing values and ensuring consistent formatting across columns. Next, we will focus on merging datasets by common keys such as institution ID or state to prepare for analysis. Initial data profiling has been conducted to understand the distributions and detect any outliers. Summary statistics for key socioeconomic variables and graduation rates have been generated to inform further analysis.

Specific relevance to project setup: Initial data cleaning will support the prelimary analysis. As mentioned above, data will be cleaned by handling missing values, ensuring consistent formats, etc. Cleaning will also involve pinpointing specific data points and key indicators that will be used when completing the analysis such as education levels, regions, poverty rates, income, emplyment, etc. Data cleaning may also involve using Python and Pandas to create different datasets that consist solely of relevant data in order to ensure smooth integration and analysis. Finally, data cleaning will also involve detecting outliers in our datasets before jumping into our integration. 

### Week 3: Data Integration and Initial Analysis

Natasha's tasks: In the process of setting up a Snakemake workflow to automate data cleaning, integration, and analysis. This will streamline reproducibility and ensure all steps can be executed seamlessly from raw data acquisition to final outputs. A primary challenge has been aligning data from different sources, particularly with variations in format and missing values. We have adjusted our integration approach to address these issues by standardizing column names for missing socioeconomic data where appropriate.

Specific relevance to project setup: Data integration will takeplace after the previous steps have been completed. This is still relevant to project set up as the workflow automation can asist with the initial steps and ensure that everything is accomplished seamlessly. This step is also important in regards to project setup as it will allow for us to have a preliminary analysis and potentially introduce areas that might need to be explored and analyzed further. 

### Week 4: Final Analysis, Visualization, and Report Preparation

Everyone: **Will begin once previous steps are completed**

## Updated Timeline
- **Data Acquisition**: Completed
- **Data Cleaning and Integration**: In progress (to be completed by Nov 20)
- **Preliminary Analysis**: To begin after integration (target completion by Nov 25)
- **Workflow Automation with Snakemake**: In progress (to be completed by Nov 27)
- **Final Analysis and Visualization**: To start by Nov 28
- **Report Drafting and Documentation**: Begin Dec 1, to be completed by Dec 8
