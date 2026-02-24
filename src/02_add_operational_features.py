import pandas as pd
import numpy as np

df = pd.read_csv("data/FINAL_MARUTI_DATASET_REALISTIC.csv")

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values(["Car_Model", "City", "Date"])

# Add operational parameters
df["Lead_Time"] = 1
df["Service_Level"] = 0.95
df["Holding_Cost_Per_Unit"] = df["Price"] * 0.02

# Previous month sales
df["Previous_Month_Sales"] = df.groupby(
    ["Car_Model", "City"]
)["Units_Sold"].shift(1)

# Rolling 3 month average
df["Rolling_3M_Avg"] = df.groupby(
    ["Car_Model", "City"]
)["Units_Sold"].transform(lambda x: x.rolling(3).mean())

# Demand variability
df["Demand_Std_Dev"] = df.groupby(
    ["Car_Model", "City"]
)["Units_Sold"].transform("std")

# Remove early null rows
df = df.dropna()

df.to_csv("data/PROJECT_STAGE2_OPERATIONAL.csv", index=False)

print("Stage 2 Complete")
print("Shape:", df.shape)