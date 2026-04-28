import pandas as pd
import numpy as np

np.random.seed(0)

data = pd.DataFrame({
    'temperature': np.random.randint(20, 100, 300),
    'voltage': np.random.randint(200, 250, 300),
    'usage_hours': np.random.randint(1, 12, 300),
    'vibration': np.random.randint(1, 10, 300),
    'humidity': np.random.randint(30, 90, 300)
})

# realistic maintenance logic
data['maintenance'] = (
    ((data['temperature'] > 75) & (data['usage_hours'] > 6)) |
    (data['voltage'] < 210) |
    (data['voltage'] > 240) |
    (data['temperature'] > 85)
).astype(int)

data.to_csv("data.csv", index=False)

print("Realistic dataset created!")