import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load financial data (Ensure your CSV has 'Year' as one column)
df = pd.read_csv("cleaned_re_extracted_data.csv")

# Calculate financial ratios
df["Current Ratio"] = df["total_current_assets"] / df["total_current_liabilities"]
df["Debt-to-Equity Ratio"] = df["total_liabilities"] / (df["total_assets"] - df["total_liabilities"])
df["Debt Ratio"] = df["total_liabilities"] / df["total_assets"]
df["Interest Coverage Ratio"] = (df["profit_before_tax"] + df["finance_cost"]) / df["finance_cost"]
df["ROA"] = (df["profit_before_tax"] / df["total_assets"]) * 100
df["ROE"] = (df["profit_before_tax"] / (df["total_assets"] - df["total_liabilities"])) * 100
df["Retained Earnings Ratio"] = (df["retained_earnings"] / df["total_assets"]) * 100

# Set style for plots
sns.set_style("whitegrid")

# Define financial ratios to visualize
ratios = ["Current Ratio", "Debt-to-Equity Ratio", "Debt Ratio", 
          "Interest Coverage Ratio", "ROA", "ROE", "Retained Earnings Ratio"]
df.to_csv(r"C:\Users\ulens\git_hub\reliance_Altzscore\financial_ratios.csv", index=False)

# Plot financial ratios over time
plt.figure(figsize=(12, 6))

for ratio in ratios:
    plt.plot(df["year"], df[ratio], marker='o', label=ratio)

plt.xlabel("year")
plt.ylabel("Ratio Value")
plt.title("Financial Ratios Trend Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
