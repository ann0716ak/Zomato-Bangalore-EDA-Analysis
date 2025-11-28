# cleaning.py
# Helper functions for cleaning the Zomato dataset

import pandas as pd
import numpy as np

def clean_rate_column(df):
    df["rate"] = df["rate"].astype(str).str.extract(r"(\d+\.\d+)")
    df["rate"] = pd.to_numeric(df["rate"], errors="coerce")
    return df

def clean_cost_column(df):
    if "approx_cost(for two people)" in df.columns:
        df["approx_cost(for two people)"] = (
            df["approx_cost(for two people)"]
            .astype(str)
            .str.replace(",", "")
        )
        df["approx_cost(for two people)"] = pd.to_numeric(
            df["approx_cost(for two people)"], errors="coerce"
        )
    return df

def drop_irrelevant_columns(df):
    cols_to_drop = ["url", "phone", "reviews_list"]
    existing = [c for c in cols_to_drop if c in df.columns]
    return df.drop(columns=existing)

