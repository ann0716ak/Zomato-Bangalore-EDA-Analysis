Zomato Bangalore Restaurants – Exploratory Data Analysis (EDA)

This project performs an end-to-end Exploratory Data Analysis (EDA) on the Zomato Bangalore Restaurants dataset, focusing on restaurant trends, pricing patterns, customer preferences, and service availability across Bangalore.
It includes problem definition, dataset cleaning, preprocessing, visual analysis, insights, and final conclusions.

Project Structure
Zomato-Bangalore-EDA-Analysis/
│
├── README.md                 <-- You are here
├── REPORTS/                  <-- Colab Notebook with markdown cells
│
├── data/
│   ├── raw/                  <-- Kaggle link to raw dataset (not uploaded due to size)
│   └── cleaned/              <-- zomato_cleaned.csv (uploaded)
│
├── notebooks/                <-- colab notebook
├── scripts/                  <-- cleaning.py and helper scripts

Project Objectives

This project aims to:

Understand customer and restaurant behavior in Bangalore

Analyze rating distribution, cost patterns, cuisines, and restaurant types

Examine service availability (online ordering, table booking)

Discover meaningful correlations between key features

Provide insights helpful for restaurant owners and food-delivery platforms

Phase 1 — Problem Definition & Dataset Selection
Problem Statement

Bangalore hosts thousands of restaurants across diverse cuisines and pricing tiers.
With increasing competition and customer expectations, restaurants require data-driven insights to:

Improve customer satisfaction

Optimize pricing

Expand service features

Understand food preferences and demand clusters

Dataset Details

Source: Kaggle

Size: 50,000+ restaurant records

Type: Mixed data (categorical + numerical + text)

Variety: Ratings, cost, votes, cuisine, location, services, etc.

Dataset Link (raw dataset):
https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data

Due to file size limits, raw dataset is not uploaded.
Instead, a reference file is added in:
/data/raw/README.md

Phase 2 — Data Cleaning & Pre-processing

Dataset issues identified and handled:

✔ Duplicate Removal

Thousands of duplicate entries were removed.

✔ Missing Value Treatment

Columns like rate, approx_cost, and cuisines were cleaned and imputed.

✔ Format Corrections

Standardized rating values

Cleaned cost field (removed commas, converted to int)

Extracted primary cuisine

✔ Removal of Irrelevant Columns

Dropped unnecessary fields:

url

phone

dish_liked

reviews_list

menu_item

✔ Feature Engineering

New helpful features were created:

Cost Category

Rating Category

Primary Cuisine

✔ Output

The cleaned dataset is saved at:
/data/cleaned/zomato_cleaned.csv

Phase 3 — Exploratory Data Analysis (EDA)

Performed Univariate, Bivariate, and Multivariate analysis.

🔹 Univariate Analysis

Distribution of ratings

Cost distribution

Popular cuisines

Restaurant types

Votes distribution

🔹 Bivariate Analysis

Cost vs Rating

Votes vs Rating

Online order vs Rating

Table booking vs Rating

🔹 Multivariate Analysis

Correlation heatmap

Location-wise restaurant density

Ratings vs Cost vs Votes (combined patterns)

Visualizations Created

10+ plots using:

Matplotlib

Seaborn

Plotly

Key Insights

Restaurant Market Insights:

Most restaurants are rated between 3.0 and 4.2

Online ordering is available in 70%+ of restaurants

Cost for two mostly ranges from ₹200–₹700

North Indian, South Indian, and Chinese are the dominant cuisines

Customer Behavior:

Higher ratings often correspond to moderate cost restaurants

Restaurants with more votes tend to have better ratings

Areas like Indiranagar, Koramangala, HSR Layout have dense restaurant clusters

Business Insights:

Adding online delivery boosts customer ratings

Multi-cuisine restaurants attract more ratings

Cost does not strongly correlate with rating (important insight!)

Conclusion

This project demonstrates a complete end-to-end data analysis pipeline:

Clear problem framing

Professional-level cleaning & preprocessing

Deep visual exploratory analysis

Actionable insights relevant to the food industry

It highlights strong skills in Python, data analytics, EDA, and visualization, making it suitable for academic evaluation, job portfolios, and GitHub showcase.

How to Use This Project
1. Clone the repository
git clone https://github.com/ann0716ak/Zomato-Bangalore-EDA-Analysis.git

2. Install requirements
pip install -r requirements.txt

3. Open the notebooks

All phases are available in:

/notebooks/

Author

Ann Mary T.J
GitHub: ann0716ak
