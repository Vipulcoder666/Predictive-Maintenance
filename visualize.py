import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.hist(data['temperature'])
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()