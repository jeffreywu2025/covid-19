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

🧩 Project Structure
covid_analysis/
│
├── covid_analysis.py       # Main analysis script
├── covid_visualizations/   # Output charts (auto-created)
│   ├── global_new_cases.png
│   ├── top_10_countries_total_cases.png
│   └── monthly_trend.png
└── README.md               # Project documentation
🛠️ Requirements
Make sure you have Python 3.8+ and install the following libraries:
pip install pandas matplotlib requests

▶️ How to Run
Clone this repository or copy the script:
git clone https://github.com/yourusername/covid-analysis.git
cd covid-analysis
Run the script:
python covid_analysis.py
The script will:
Download the latest COVID-19 dataset
Clean and analyze the data
Generate visualizations inside covid_visualizations/

📊 Example Output
Global Daily New Cases
Top 10 Countries by Total Cases
Monthly Average Cases Trend
