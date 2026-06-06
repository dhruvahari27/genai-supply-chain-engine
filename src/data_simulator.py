import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_supply_chain_data():
    np.random.seed(42)
    start_date = datetime(2023, 1, 1)
    total_days = 1095  # 3 years of daily history
    dates = [start_date + timedelta(days=i) for i in range(total_days)]
    
    # 1. Generate Realistic Demand: Base + Growth Trend + Weekly Seasonality + Random Noise
    base_demand = 200
    trend = np.linspace(0, 80, total_days)
    seasonality = 40 * np.sin(2 * np.pi * np.array(range(total_days)) / 7)
    noise = np.random.normal(0, 18, total_days)
    
    demand = base_demand + trend + seasonality + noise
    
    # 2. Inject a major supply chain anomaly (simulating a brutal Q3 heatwave in Year 3)
    # This represents a sudden 15-day spike that standard models fail to explain without context
    demand[950:965] += 130 
    
    # Structure into DataFrame
    df = pd.DataFrame({
        'date': dates, 
        'demand': np.clip(demand, 15, None).astype(int) # Ensure no negative demand
    })
    df.to_csv('data/historical_demand.csv', index=False)
    
    # 3. Create a Vendor Catalog with varying lead times and pricing matrix
    vendors = pd.DataFrame({
        'vendor_id': ['VND001', 'VND002'],
        'vendor_name': ['Alpha Logistics (Standard)', 'Beta Prime Corp (Express)'],
        'lead_time_days': [5, 2],         # VND001 is slow but cheap, VND002 is fast but pricey
        'unit_cost': [12.50, 18.00],       # Express carries a premium cost
        'reliability_score': [0.91, 0.98]  # Express is highly dependable
    })
    vendors.to_csv('data/vendor_catalog.csv', index=False)
    
    print("✅ Success: Created 'data/historical_demand.csv' and 'data/vendor_catalog.csv'!")

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    generate_supply_chain_data()