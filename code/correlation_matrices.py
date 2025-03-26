import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (Ensure 'Year' column exists)
df = pd.read_csv(r"C:\Users\ulens\git_hub\reliance_Altzscore\financial_ratios.csv")

# Select only financial ratio columns
ratios = ["Current Ratio", "Debt-to-Equity Ratio", "Debt Ratio", 
          "Interest Coverage Ratio", "ROA", "ROE", "Retained Earnings Ratio"]

df_ratios = df[ratios]

# Compute correlation matrix
corr_matrix = df_ratios.corr()

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Financial Ratio Correlation Heatmap")
plt.show()