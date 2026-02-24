import pandas as pd
import numpy as np

df = pd.read_csv("data/PROJECT_STAGE3_FORECAST.csv")

# =========================
# Inventory Calculations
# =========================

Z = 1.65  # 95% service level

df["Safety_Stock"] = Z * df["Demand_Std_Dev"]

df["Reorder_Point"] = df["Forecasted_Demand"] + df["Safety_Stock"]

df["Inventory_Gap"] = df["Reorder_Point"] - df["Units_Sold"]

df["Holding_Cost_Impact"] = (
    df["Inventory_Gap"].clip(lower=0) *
    df["Holding_Cost_Per_Unit"]
)

# =========================
# Risk Alert System
# =========================

def risk_alert(row):
    if row["Demand_Std_Dev"] > row["Rolling_3M_Avg"] * 0.5 and row["Inventory_Gap"] < 0:
        return "High Stockout Risk"
    elif row["Inventory_Gap"] > 0:
        return "Excess Inventory Risk"
    else:
        return "Stable"

df["Risk_Alert"] = df.apply(risk_alert, axis=1)

# =========================
# Profit Impact Estimation
# =========================

# Assume 8% profit margin
df["Profit_Per_Unit"] = df["Price"] * 0.08

# Lost profit due to stock-out
df["Lost_Profit"] = (
    df["Inventory_Gap"].clip(upper=0).abs() *
    df["Profit_Per_Unit"]
)

# Capital blocked in excess stock
df["Blocked_Capital"] = (
    df["Inventory_Gap"].clip(lower=0) *
    df["Price"]
)

# =========================
# Save Final Dataset
# =========================

df.to_csv("data/FINAL_PROJECT_COMPLETE.csv", index=False)

print("Inventory + Risk + Profit calculations complete")
print("Final rows:", df.shape[0])