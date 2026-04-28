import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

# user input
temp = int(input("Enter temperature: "))
volt = int(input("Enter voltage: "))
hours = int(input("Enter usage hours: "))

prediction = model.predict([[temp, volt, hours]])

if prediction[0] == 1:
    print("Maintenance Required")
else:
    print("No Maintenance Needed")