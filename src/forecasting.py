import torch
import pandas as pd
import numpy as np
from chronos import ChronosPipeline

def generate_forecast(history_path='data/historical_demand.csv', horizon=14):
    print("🧠 Initializing Chronos Foundation Model...")
    
    # 1. Load data and extract the most recent 30 days as context window
    df = pd.read_csv(history_path)
    context_data = df['demand'].values[-30:]
    context = torch.tensor(context_data, dtype=torch.float32)
    
    # 2. Instantiate the pretrained model pipeline
    pipeline = ChronosPipeline.from_pretrained(
        "amazon/chronos-t5-base",
        device_map="cpu",  # Set to "cuda" if your machine has a dedicated Nvidia GPU
        torch_dtype=torch.float32,
    )
    
    # 3. Run zero-shot inference
    # Chronos generates multiple probabilistic trajectories (samples)
    forecast_samples = pipeline.predict(context, horizon)
    
    # 4. Extract Quantiles across trajectories
    # 50th percentile = Median (Expected Forecast)
    # 10th and 90th percentiles define boundaries for risk mapping
    low_bound, median_forecast, high_bound = np.percentile(
        forecast_samples[0].numpy(), [10, 50, 90], axis=0
    )
    
    return {
        "low": low_bound.astype(int),
        "median": median_forecast.astype(int),
        "high": high_bound.astype(int)
    }

if __name__ == "__main__":
    forecasts = generate_forecast()
    print("\n🔮 14-Day Demand Forecast Vector (Median):")
    print(forecasts["median"])
    print("\n🛡️ High-Risk Boundary Vector (90th Percentile):")
    print(forecasts["high"])
    