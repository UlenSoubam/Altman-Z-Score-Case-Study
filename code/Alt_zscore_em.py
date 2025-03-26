import pandas as pd
import numpy as np


#import the cleaned data
df = pd.read_csv("cleaned_re.csv")

# Required columns for Altman Z-Score EM calculation
REQUIRED_COLUMNS = [
    "year", "total_current_assets", "total_non_current_assets", "total_assets",
    "total_non_current_liabilities", "total_current_liabilities", "total_liabilities", "retained_earnings", "profit_before_tax",
    "finance_cost"]

#Make sure to use only the relevant data
df = df[REQUIRED_COLUMNS]

#to remove unnecessary index displayed
df = df.loc[:, ~df.columns.str.contains('Unnamed')]

#now we need to find working capital, EBIT & book value of equity
df["book_value_equity"] = df["total_assets"]- df["total_liabilities"]
df["ebit"] = df["finance_cost"] + df["profit_before_tax"]
df["working_capital"]= df["total_current_assets"] - df["total_current_liabilities"]

#now to calculate financial ratios required
df["X1"] = df["working_capital"] / df["total_assets"] #Liquidity ratio
df["X2"] = df["retained_earnings"] / df["total_assets"] #profitability ratio
df["X3"] = df["ebit"] / df["total_assets"] #operating efficiency ratio
df["X4"] = df["book_value_equity"] / df["total_liabilities"] #solvency ratio


#Calculating Z score
df["Altman_Zscore_EM"] = (6.56 * df["X1"]) + (3.26 * df["X2"]) + (6.72 * df["X3"]) + (1.05 * df["X4"])
#round decimal to 2 place using numpy
df["Altman_Zscore_EM"] = np.round(df["Altman_Zscore_EM"], 2)
#export required columns for data vizualization
df[["year", "X1", "X2", "X3", "X4", "Altman_Zscore_EM"]].to_csv("alt_zscore_viz.csv", index=False)

