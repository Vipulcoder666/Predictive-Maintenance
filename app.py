from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# model load
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return "Predictive Maintenance API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # input extract
        temp = data['temperature']
        volt = data['voltage']
        hours = data['usage_hours']
        vibration = data['vibration']
        humidity = data['humidity']

        # prediction
        prediction = model.predict([[temp, volt, hours, vibration, humidity]])

        result = "Maintenance Required" if prediction[0] == 1 else "No Maintenance Needed"

        return jsonify({
            "prediction": int(prediction[0]),
            "message": result
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)