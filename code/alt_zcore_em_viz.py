import seaborn as sns
import pandas as pd #to read manipulate dataset
import numpy as np
import matplotlib.pyplot as plt  # Import Matplotlib for visualization

# Load the dataset
df = pd.read_csv("alt_zscore_viz.csv")

# Plot the Z''-Score trend
plt.figure(figsize=(10, 5)) #10 inch wide and 5 inch high #prevents default small figure
#plt.plot(x, y, marker, linestyle, color, label)
plt.plot(df["year"], df["Altman_Zscore_EM"], marker="o", linestyle="-", color="blue", label="Altman Z''-Score")

# Add labels for each data point
#enumerate(df["Altman_Zscore_EM"]) → Loops over each Z
#y = df["Altman_Zscore_EM"][i] + 0.1 → Position slightly above the point.
#plt.text(x, y, text, ha="center", fontsize=9) → Adds text near each point.
for i, txt in enumerate(df["Altman_Zscore_EM"]):
    plt.text(df["year"][i], df["Altman_Zscore_EM"][i] + 0.1, round(txt, 2), ha="center", fontsize=9)

#plt.axhspan(y_min, y_max, color, alpha, label) → Shades a horizontal area from y_min to y_max.alpha=0.2 → Transparency level (0 = invisible, 1 = solid color).
plt.axhspan(2.6, max(df["Altman_Zscore_EM"]) + 1, color='green', alpha=0.2, label="Safe Zone (Z'' > 2.6)")
plt.axhspan(1.1, 2.6, color='yellow', alpha=0.2, label="Grey Zone (1.1 < Z'' < 2.6)")
plt.axhspan(min(df["Altman_Zscore_EM"]) - 1, 1.1, color='red', alpha=0.2, label="Distress Zone (Z'' < 1.1)")

# plt.axhline(y, color, linestyle, linewidth) → Draws a horizontal line.
plt.axhline(y=2.6, color="green", linestyle="--", linewidth=1)  # Safe Zone boundary
plt.axhline(y=1.1, color="red", linestyle="--", linewidth=1)  # Distress Zone boundary
#plt.legend() → Shows a legend (explains the chart elements).plt.grid(True)Enables grid lines.
plt.xlabel("Year")
plt.ylabel("Altman Z''-Score")
plt.title("Altman Z''-Score Trend Over 10 Years")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
