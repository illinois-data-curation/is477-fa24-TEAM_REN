# Overview: The overall goal of our project

Throughout the United States, public school education exists to provide all children with a form of education despite the different socioeconomic classes they come from. However, this apparent equality of education among students across the US still struggles with inequitities as life within different socioeconomic brackets can still result in different educational outcomes for students. For example, access to private tutors and personalized help is not widely accessible to each student in the country. Additionally, regional factors can contribute to these differences due to inconsistencies in the standard of living among different regions of the United States. 

The goal of our project is to analyze the relationship between socioeconomic factors and education outcomes across different regions of the United States. By integrating data on socioeconomic indicators from the U.S. Census Bureau with education statistics from the National Center for Education Statistics (NCES), we aim to uncover patterns and correlations that may reveal how factors like income and employment impact educational achievement. This project will involve programmatically acquiring, integrating, and analyzing data from two sources with different formats and licenses. We will use Python, SQL, and visualization techniques to create an automated, reproducible workflow, producing insights that can inform discussions on education equity and policy interventions.

## Research Question(s): What is/are the question(s) you intend to address?

1. How do socioeconomic factors (e.g., income, poverty rates, employment) influence education outcomes (e.g., graduation rates, test scores) across different U.S. regions?
2. Are there regional patterns in how socioeconomic factors correlate with educational achievements, and what might these patterns indicate about resource allocation or policy needs?

## Team: Clearly define team member roles and responsibilities 

Evelina : Will primarily focus on documentation and data acquisition. They will lead the initial stages of the project in terms of data acquisiton and then throughout the project, will continue to support in the cleaning and integration processes as well as documenting all parts of this project. . 

Richa: Will primarily focus on data cleaning. They will initially sort through the datasets (acquired by Team Member #1) and ensure that all neccessary information exists. Then, they will continue the cleaning process by splitting the datasets in order to focus on the relevant data for our project. Finally, they will also help with the data integration process. 

Natasha: Will primarily focus on spearheading the data integration section. While all team members will help with writing the code and doing the analysis, Team Member #3 will break down the neccessary information to analyze and lead the integration and coding sections of this project. Team Member #3 will also support with the cleaning and acquisiton process and will receive support for the integration process. 

**Team Member roles will be further detailed and explained in the project plan. More information can be found below in the timeline section**

## Datasets: Identify and describe the two datasets that you will use. If you are looking for ideas for datasets to use, please reach out via Campuswire.

### Poverty Statistics: ACS (API Data)

This dataset is extremely comprehensive and consists of all relevant factors needed to analyze socieconomic demographics. This data set comes from the US Census Bureau, specifically the American Community Survey (ACS). We will specifically be looking at the various races outline (including mixed races) to further understand the different socioeconomic factors that may influence education. Additionally, we will take a close look at the small area income and poverty estimates (SAIPE) with which we wil gather data on the total number of people facing poverty, the number of children in households facing poverty, median houshold income, geographical regions that primarily face poverty, and other variables that may impact the socioeconomic factors of a houshold. Data will be further looked into and analyzed as the project continues, where more variables to analyze may or may not appear. 

### College Completion Data Set (Non-API Data from Kaggle.com)

This data set specifically documents whether or not college was completed by different individuals. Among this data, it specifically outlines the different aspects of a university like the cohort sizes, states, cities, type of university (public or private), and whether or not it is an HBCU (historically Black college or University) as well as a flagship university. Analyzing the higher-education pathways of students that come from various socioeconomic backgrounds can help us understand how education (starting from elementary school onwards) changes based off of different socioeconomic factors.

**It is important to note that these two data sets are the initial data sets and more data may be required to complete a deeper analysis**

## Timeline: Document the plan and timeline for implementing your project including who will complete each task.**

### Week 1: Project Setup and Initial Data Acquisition

Evelina: Begin acquiring the poverty and income data from the U.S. Census API.

Natasha: Set up the project repository and ensure all team members have access. 

Richa: Begin researching cleaning strategies for both datasets and setting up initial cleaning scripts for use in later stages.

All Team Members: Meet to clarify the project’s objectives and develop a clear plan for how the datasets will be analyzed in relation to the research questions.

### Week 2: Data Cleaning and Initial Exploration

Richa: Clean the poverty dataset by identifying relevant variables (income, child poverty, geographic factors). Handle missing values, remove unnecessary columns, and ensure data consistency.

Natasha: Clean the college completion dataset, organizing it into usable sections, handling missing or inconsistent values, and preparing it for integration.

Evelina: Document the data-cleaning process and ensure reproducibility in the project repository. Begin exploratory data analysis on both datasets to identify key trends.

### Week 3: Data Integration and Initial Analysis

Natasha: Lead the data integration, combining datasets through geographic or socioeconomic variables. Ensure the integration aligns with the research questions.

Richa: Support Natasha in testing and validating the integration process, troubleshooting any issues that arise.

Evelina: Continue to document the integration process, create visualizations of the merged dataset, and begin drafting initial analysis.

All Team Members: Begin analyzing correlations between socioeconomic factors and educational outcomes. Discuss preliminary findings and adjust cleaning or integration steps if needed.

### Week 4: Final Analysis, Visualization, and Report Preparation

Natasha: Finalize the data analysis, focusing on extracting insights related to regional patterns and their educational implications.

Richa: Lead the creation of visualizations, focusing on clear representation of key findings such as socioeconomic disparities and educational outcomes across regions.

Evelina: Finalize documentation of the entire project process and begin writing the final report.

All Team Members: Collaborate on the final report. Ensure all code, analysis, and visualizations are complete and organized.