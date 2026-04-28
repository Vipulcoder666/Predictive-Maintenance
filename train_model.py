import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# load data
data = pd.read_csv("data.csv")

X = data[['temperature', 'voltage', 'usage_hours']]
y = data['maintenance']

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")