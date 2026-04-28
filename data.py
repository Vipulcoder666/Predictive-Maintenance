import pandas as pd
import numpy as np

np.random.seed(0)

data = pd.DataFrame({
    'temperature': np.random.randint(20, 100, 200),
    'voltage': np.random.randint(200, 250, 200),
    'usage_hours': np.random.randint(1, 10, 200)
})

data['maintenance'] = (
    (data['temperature'] > 70) | 
    (data['usage_hours'] > 7)
).astype(int)

# save data
data.to_csv("data.csv", index=False)

print("Data created successfully!")