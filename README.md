Dealer-Level Sales Forecasting and Inventory Optimization

This project builds a machine learning system to forecast car sales demand at dealer level and optimize inventory decisions using operational analytics.

The objective is to reduce stockouts, minimize overstock risk, and improve profit visibility using predictive modeling.

Problem Statement

Automotive dealers face two major challenges:

• Demand uncertainty
• Inventory imbalance

Overstock increases holding cost.
Understock leads to lost sales.

This system predicts dealer-level demand and recommends optimal inventory decisions.

Project Pipeline

Stage 1
Cleaned structured sales dataset.

Stage 2
Added operational features:

• Previous month sales
• Rolling 3-month average
• Demand variability
• Holding cost per unit
• Service level

Stage 3
Built Random Forest demand forecasting model.

Model Performance:

• MAE ≈ 3900 units
• R2 ≈ 0.92

Feature Importance Ranking:

• Marketing Spend
• Rolling 3M Average
• Previous Month Sales
• Price
• Discount
• Fuel Price

Stage 4
Inventory Optimization Engine:

• Safety Stock calculation
• Reorder Point calculation
• Inventory Gap analysis
• Risk classification
• Profit impact estimation

Stage 5
Scenario Simulation:

Simulated fuel price shock to analyze impact on demand and inventory.

Technologies Used

• Python
• Pandas
• NumPy
• Scikit-learn
• Random Forest Regressor

Project Structure

data/
Contains datasets for each stage.

src/
Contains pipeline scripts:

02_add_operational_features.py
03_forecast_model.py
04_inventory_engine.py
05_scenario_simulation.py

Business Impact

This system enables:

• Data-driven stocking decisions
• Reduced capital blockage
• Improved service level
• Forecast-based planning

How to Run

Install dependencies
pip install -r requirements.txt

Run pipeline

python src/02_add_operational_features.py
python src/03_forecast_model.py
python src/04_inventory_engine.py
python src/05_scenario_simulation.py

Author

Himanshu 
BTech Computer Science
