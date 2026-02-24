import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/PROJECT_STAGE2_OPERATIONAL.csv")

X = df[[
    "Price",
    "Discount",
    "Marketing_Spend",
    "Fuel_Price",
    "Previous_Month_Sales",
    "Rolling_3M_Avg"
]]

y = df["Units_Sold"]

model = RandomForestRegressor(n_estimators=120, random_state=42)
model.fit(X, y)

df_scenario = df.copy()
df_scenario["Fuel_Price"] *= 1.10

df_scenario["Scenario_Forecast"] = model.predict(df_scenario[X.columns])

df_scenario.to_csv("data/SCENARIO_SIMULATION_OUTPUT.csv", index=False)

print("Scenario simulation complete")
print("Rows:", df_scenario.shape[0])
