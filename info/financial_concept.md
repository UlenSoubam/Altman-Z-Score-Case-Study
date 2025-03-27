## **1. Understanding the Altman Z-Score**  
The **Altman Z-Score** is a financial model developed by Edward Altman in 1968 to predict corporate bankruptcy and financial distress. It uses a weighted combination of financial ratios to assess the probability of a company defaulting on its obligations. 

For **emerging markets**, the model is adjusted due to differences in capital structures, economic stability, and risk factors. The **Z-Score for Emerging Markets (EM Z-Score)** typically includes modified weightings for key financial ratios.

---

## **2. Ratios & Weights Used in the Z-Score Model**  
For **public manufacturing firms**, the original Altman Z-Score formula is:  
```math
Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5
```
where:
- **X₁ = (Working Capital / Total Assets)**  
- **X₂ = (Retained Earnings / Total Assets)**  
- **X₃ = (EBIT / Total Assets)**  
- **X₄ = (Market Value of Equity / Total Liabilities)**  
- **X₅ = (Sales / Total Assets)**  

For **emerging markets**, the modified formula is:  
```math
Z' = 6.56X_1 + 3.26X_2 + 6.72X_3 + 1.05X_4
```
where:  
- **X₁ = (Working Capital / Total Assets)**  
- **X₂ = (Retained Earnings / Total Assets)**  
- **X₃ = (EBIT / Total Assets)**  
- **X₄ = (Book Value of Equity / Total Liabilities)**  

This adjustment accounts for **greater volatility in emerging markets**, where book values are more stable than market values.

---

## **3. Key Financial Elements & Their Role in Z-Score and Other Ratios**

### **(A) Balance Sheet Components**
- **Total Non-Current Assets**: Long-term assets like property, plant, and equipment (PP&E), intangible assets, and investments.  
- **Total Current Assets**: Cash, accounts receivable, inventory, and short-term investments.  
- **Total Assets**: Sum of current and non-current assets.  
- **Total Non-Current Liabilities**: Long-term debt, pension obligations, deferred tax liabilities.  
- **Total Current Liabilities**: Short-term obligations like accounts payable, short-term debt, and accrued expenses.  
- **Total Liabilities**: Sum of current and non-current liabilities.  

### **(B) Income Statement Components**
- **Retained Earnings**: Profits retained in the company rather than distributed as dividends. 
- **Profit Before Tax (PBT)**: Earnings before tax obligations.  
- **Finance Cost**: Interest payments on debt.  
- **EBIT (Earnings Before Interest & Taxes)**: Operational profitability measure.  

---

## **4. Financial Ratios & Their Interconnections**

### **(A) Liquidity & Solvency Ratios**
- **Current Ratio** = (Total Current Assets / Total Current Liabilities)  
  - Measures a company’s ability to cover short-term liabilities.
  - A lower value indicates liquidity risk, increasing bankruptcy probability in **Altman Z-score calculations**.  

- **Debt to Equity Ratio** = (Total Liabilities / Book Value of Equity)  
  - Indicates financial leverage. Higher values signal more debt, increasing bankruptcy risk.  
  - Used indirectly in the **EM Z-score** via the **Book Value of Equity/Total Liabilities** component.  

- **Debt Ratio** = (Total Liabilities / Total Assets)  
  - Measures how much of the company’s assets are financed by debt.  
  - A high debt ratio **lowers the Altman Z-score**, increasing financial distress probability.  

### **(B) Profitability & Coverage Ratios**
- **Interest Coverage Ratio** = (EBIT / Finance Cost)  
  - Measures how easily a company can pay interest on its debt.  
  - A lower ratio means higher default risk, affecting the **Z-score’s EBIT/Total Assets component**.  

- **Return on Assets (ROA)** = (Net Income / Total Assets)  
  - Indicates profitability relative to assets. **ROA is similar to EBIT/Total Assets, which is in the Z-score formula.**  

- **Return on Equity (ROE)** = (Net Income / Book Value of Equity)  
  - Measures profitability for shareholders.  
  - A declining ROE suggests financial instability, making it an indirect contributor to **bankruptcy risk assessment**.  

- **Retained Earnings Ratio** = (Retained Earnings / Total Assets)  
  - Used in the Z-score formula as **X₂**. A low ratio means past earnings have not been retained, increasing financial risk.
---
## **5. Summary: Connecting Everything to the Altman Z-Score**
The **Altman Z-score** synthesizes multiple financial ratios to determine bankruptcy risk. The core logic behind its components:  
- **Liquidity (Current Ratio, Working Capital/Total Assets)** – Measures short-term financial health.
-  **Leverage (Debt to Equity, Debt Ratio, Book Value of Equity/Total Liabilities)** – Assesses financial stability and solvency.  
-  **Profitability (ROA, EBIT/Total Assets, Interest Coverage Ratio, Retained Earnings Ratio)** –Indicates earnings strength and long-term sustainability.  

A **low Z-score** suggests **high bankruptcy risk**, while a **high Z-score** indicates **financial stability**. Adjustments for **emerging markets** refine the formula to reflect economic conditions, emphasizing **book equity instead of market equity** for financial risk assessment.  

---

