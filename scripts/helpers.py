# helpers.py
# Utility helper functions for EDA and preprocessing

import seaborn as sns
import matplotlib.pyplot as plt

def show_missing_values(df):
    return df.isnull().sum().sort_values(ascending=False)

def plot_count(df, column, title=""):
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x=column)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

def plot_distribution(df, column, title=""):
    plt.figure(figsize=(8,5))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(title)
    plt.show()
