import pickle

model = pickle.load(open("model.pkl", "rb"))

temp = int(input("Enter temperature: "))
volt = int(input("Enter voltage: "))
hours = int(input("Enter usage hours: "))
vibration = int(input("Enter vibration level: "))
humidity = int(input("Enter humidity: "))

prediction = model.predict([[temp, volt, hours, vibration, humidity]])

if prediction[0] == 1:
    print("⚠️ Maintenance Required")
else:
    print("✅ No Maintenance Needed")