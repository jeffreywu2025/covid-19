🦠 COVID-19 Data Analysis using Pandas & Matplotlib

📘 Overview
This project performs data analysis and visualization on the global COVID-19 dataset from Our World in Data (OWID).
It uses Python, Pandas, and Matplotlib to clean, analyze, and visualize trends in COVID-19 cases worldwide.

🚀 Features
Automated dataset loading directly from the OWID public repository
Data cleaning and preprocessing:
Removes invalid or aggregate data
Handles missing values intelligently
Converts and validates date fields
Ensures numerical consistency (non-negative case counts)
Exploratory Data Analysis (EDA):
Calculates mean, median, maximum, and total cases
Computes correlation between new cases and deaths
Displays dataset coverage and statistics

Visualizations:
📈 Global daily new cases trend (line chart)
📊 Top 10 countries by total cases (bar chart)
🗓️ Monthly average trend of new cases (line chart)
All charts are automatically saved in the covid_visualizations/ directory.

▶️ How to Run
1.Clone this repository or copy the script:
git clone https://github.com/yourusername/covid-analysis.git
cd covid-analysis
2.Run the script:
python covid_analysis.py
3.The script will:
-Download the latest COVID-19 dataset
-Clean and analyze the data
-Generate visualizations inside covid_visualizations/

📊 Example Output
-Global Daily New Cases
<img width="3568" height="1768" alt="global_new_cases" src="https://github.com/user-attachments/assets/a30d5b2a-9533-427f-90c4-97598a9b9344" />
-Top 10 Countries by Total Cases
<img width="3568" height="2068" alt="top_10_countries_total_cases" src="https://github.com/user-attachments/assets/cc8f3a73-0ed6-4bb4-9410-197101a9fb1d" />
-Monthly Average Cases Trend
<img width="3568" height="1768" alt="monthly_trend" src="https://github.com/user-attachments/assets/54a4dde1-e243-4cda-ab7c-0aa60ba090c0" />



