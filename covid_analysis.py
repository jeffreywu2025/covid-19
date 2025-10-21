# Description: Analysis of COVID-19 dataset using pandas and matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime
import requests
from urllib.error import URLError
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings for this specific case
warnings.filterwarnings('ignore', category=InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# ----------------------------------------
# 1. Load Dataset
# ----------------------------------------


def load_dataset(url):
    try:
        print("Loading dataset...")
        # Download the data using requests with SSL verification
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            raise URLError(f"URL returned status code {response.status_code}")

        # Create a DataFrame from the downloaded content
        from io import StringIO
        df = pd.read_csv(StringIO(response.text))
        print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except (URLError, requests.RequestException) as e:
        print(f"Error loading dataset: {e}")
        print("Please check your internet connection or try again later.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The dataset is empty")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error loading dataset: {e}")
        sys.exit(1)


# Load the dataset
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = load_dataset(url)

# ----------------------------------------
# 2. Clean Dataset
# ----------------------------------------


def clean_dataset(df):
    try:
        print("\nCleaning dataset...")

        # Make a copy to avoid modifying the original dataframe
        df_clean = df.copy()

        # Keep only rows with continent data (remove aggregates like 'World')
        df_clean = df_clean[df_clean['continent'].notna()]

        # Convert date to datetime
        df_clean['date'] = pd.to_datetime(df_clean['date'])

        # Handle missing values more carefully
        # Fill missing numerical values with 0
        numeric_columns = df_clean.select_dtypes(
            include=['float64', 'int64']).columns
        df_clean[numeric_columns] = df_clean[numeric_columns].fillna(0)

        # Fill missing categorical values with 'Unknown'
        categorical_columns = df_clean.select_dtypes(
            include=['object']).columns
        df_clean[categorical_columns] = df_clean[categorical_columns].fillna(
            'Unknown')

        # Remove any rows with invalid dates
        df_clean = df_clean[df_clean['date'].notna()]

        # Ensure total_cases and new_cases are non-negative
        df_clean['total_cases'] = df_clean['total_cases'].clip(lower=0)
        df_clean['new_cases'] = df_clean['new_cases'].clip(lower=0)

        print(f"Dataset cleaned. Remaining rows: {df_clean.shape[0]}")
        return df_clean

    except Exception as e:
        print(f"Error cleaning dataset: {e}")
        sys.exit(1)


# Clean the dataset
df = clean_dataset(df)

# ----------------------------------------
# 3. Basic Analysis
# ----------------------------------------


def perform_analysis(df):
    try:
        print("\n--- Basic Analysis ---")

        # Calculate basic statistics
        mean_cases = df['new_cases'].mean()
        median_cases = df['new_cases'].median()
        max_cases = df['new_cases'].max()
        total_cases_worldwide = df['total_cases'].max()

        # Calculate correlation between new cases and deaths
        correlation = df[['new_cases', 'new_deaths']].corr()

        # Get the date range of the dataset
        date_range = df['date'].max() - df['date'].min()

        # Print results
        print(f"Dataset covers {date_range.days} days")
        print(f"Mean daily new cases: {mean_cases:,.2f}")
        print(f"Median daily new cases: {median_cases:,.2f}")
        print(f"Maximum daily new cases: {max_cases:,.2f}")
        print(f"Total cases worldwide: {total_cases_worldwide:,.2f}")
        print("\nCorrelation between new cases and deaths:")
        print(correlation)

        return {
            'mean_cases': mean_cases,
            'median_cases': median_cases,
            'max_cases': max_cases,
            'total_cases': total_cases_worldwide,
            'correlation': correlation
        }

    except Exception as e:
        print(f"Error performing analysis: {e}")
        return None


# Perform analysis
analysis_results = perform_analysis(df)

# ----------------------------------------
# 4. Visualizations
# ----------------------------------------


def create_visualizations(df):
    try:
        print("\nGenerating visualizations...")

        # Create output directory if it doesn't exist
        import os
        output_dir = "covid_visualizations"
        os.makedirs(output_dir, exist_ok=True)

        # (1) Line Chart: Global new cases over time
        print("Generating global new cases trend chart...")
        global_cases = df.groupby('date')['new_cases'].sum()

        plt.figure(figsize=(12, 6))
        plt.plot(global_cases.index, global_cases.values,
                 color='blue', linewidth=2)
        plt.title("Global Daily COVID-19 New Cases", pad=20, fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("New Cases", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "global_new_cases.png"),
                    dpi=300, bbox_inches='tight')
        plt.close()

        # (2) Bar Chart: Top 10 countries by total cases
        print("Generating top 10 countries chart...")
        top_countries = df.groupby('location')['total_cases'].max(
        ).sort_values(ascending=False).head(10)

        plt.figure(figsize=(12, 7))
        ax = top_countries.plot(kind='bar', color='orange')
        plt.title("Top 10 Countries by Total COVID-19 Cases",
                  pad=20, fontsize=14)
        plt.ylabel("Total Cases", fontsize=12)
        plt.xlabel("Country", fontsize=12)
        plt.xticks(rotation=45, ha='right')

        # Add value labels on top of each bar
        for i, v in enumerate(top_countries):
            ax.text(i, v, f'{v:,.0f}',
                    ha='center', va='bottom', fontsize=10)

        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(os.path.join(
            output_dir, "top_10_countries_total_cases.png"), dpi=300, bbox_inches='tight')
        plt.close()

        # (3) New visualization: Monthly trend
        print("Generating monthly trend chart...")
        df['month'] = df['date'].dt.to_period('M')
        monthly_cases = df.groupby('month')['new_cases'].mean()

        plt.figure(figsize=(12, 6))
        monthly_cases.plot(kind='line', marker='o')
        plt.title("Average Daily Cases by Month", pad=20, fontsize=14)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Average Daily Cases", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "monthly_trend.png"),
                    dpi=300, bbox_inches='tight')
        plt.close()

        print(
            f"\nAll visualizations saved successfully in '{output_dir}' directory.")

    except Exception as e:
        print(f"Error creating visualizations: {e}")


# Generate visualizations
create_visualizations(df)
