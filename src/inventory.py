import pandas as pd
import numpy as np

def calculate_inventory_metrics(history_path='data/historical_demand.csv', vendor_path='data/vendor_catalog.csv', current_stock=250):
    print("🧮 Executing Supply Chain Optimization Math...")
    
    # 1. Load Data
    df = pd.read_csv(history_path)
    vendors = pd.read_csv(vendor_path)
    
    # Calculate historical baseline metrics (last 90 days for recent operational baseline)
    recent_history = df.tail(90)
    avg_daily_demand = recent_history['demand'].mean()
    std_daily_demand = recent_history['demand'].std()
    
    # Z-score for 95% service level confidence
    Z_score = 1.65 
    
    inventory_recommendations = {}
    
    # 2. Evaluate boundaries for each vendor options
    for _, row in vendors.iterrows():
        v_id = row['vendor_id']
        v_name = row['vendor_name']
        lead_time = row['lead_time_days']
        
        # Scale standard deviation over the vendor's specific lead time
        sigma_lt = std_daily_demand * np.sqrt(lead_time)
        
        # Calculate Safety Stock (SS) and Reorder Point (ROP)
        safety_stock = Z_score * sigma_lt
        reorder_point = (avg_daily_demand * lead_time) + safety_stock
        
        # Check if the warehouse needs to trigger a restock request right now
        trigger_reorder = current_stock <= reorder_point
        
        inventory_recommendations[v_id] = {
            "vendor_name": v_name,
            "lead_time_days": int(lead_time),
            "avg_daily_demand": round(avg_daily_demand, 2),
            "safety_stock": int(np.ceil(safety_stock)),
            "reorder_point": int(np.ceil(reorder_point)),
            "current_stock": current_stock,
            "trigger_action": trigger_reorder
        }
        
    return inventory_recommendations

if __name__ == "__main__":
    # Test with a simulated warehouse running thin on stock (250 units left)
    metrics = calculate_inventory_metrics(current_stock=250)
    
    for v_id, data in metrics.items():
        print(f"\n🏢 Strategy Profile for {data['vendor_name']} ({v_id}):")
        print(f"  ▪️ Safety Stock Cushion Needed: {data['safety_stock']} units")
        print(f"  ▪️ Reorder Point (ROP Threshold): {data['reorder_point']} units")
        print(f"  ▪️ Status: {'🚨 TRIGGER ORDER AGENT' if data['trigger_action'] else '✅ Stock Levels Safe'}")