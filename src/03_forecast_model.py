import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("data/PROJECT_STAGE2_OPERATIONAL.csv")

pd.read_csv("data/PROJECT_STAGE2_OPERATIONAL.csv")

X = df[[
    "Price",
    "Discount",
    "Marketing_Spend",
    "Fuel_Price",
    "Previous_Month_Sales",
    "Rolling_3M_Avg"
]]

y = df["Units_Sold"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=120, random_state=42)
model.fit(X_train, y_train)
importances = model.feature_importances_
features = X.columns

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance Ranking:\n")
print(importance_df.reset_index(drop=True))

importance_df.to_csv("FEATURE_IMPORTANCE.csv", index=False)

pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred))
print("R2:", r2_score(y_test, pred))

df["Forecasted_Demand"] = model.predict(X)

df.to_csv("data/PROJECT_STAGE3_FORECAST.csv", index=False)

print("Stage 3 Complete")