#  Predictive Maintenance System (ML + Flask)

---

##  Overview

This project is a Machine Learning-based system that predicts whether an appliance (such as an AC) requires maintenance based on sensor data.

The system uses features like:

* Temperature
* Voltage
* Usage hours
* Vibration
* Humidity

It demonstrates how machine learning models can be trained and deployed using a REST API.

---

##  Objective

To build a system that can:

* Predict maintenance needs before failure
* Simulate real-world sensor-based decision making
* Provide real-time predictions via API

---

##  How It Works

1. Synthetic sensor data is generated
2. A machine learning model is trained on this data
3. The trained model learns patterns
4. A Flask API is created
5. Input data is sent to the API
6. The model returns a prediction

---

##  Project Structure

predictive-maintenance/
│
├── data.py              → Generates dataset
├── train_model.py       → Trains ML model
├── visualize.py         → Data visualization
├── predict.py           → Manual prediction
├── app.py               → Flask API
├── data.csv             → Generated dataset
├── model.pkl            → Trained model
└── README.md
<img width="225" height="212" alt="image" src="https://github.com/user-attachments/assets/eac4548c-8514-4e22-8087-6b5313b5491f" />


---

##  Installation

Install required libraries:

pip install pandas numpy scikit-learn matplotlib flask

---

##  Running the Project

### 1. Generate Dataset

python data.py

---

### 2. Train Model

python train_model.py

---

### 3. Visualize Data (Optional)

python visualize.py

---

### 4. Start Flask Server

python app.py

Server runs at:

http://127.0.0.1:5000

---

##  API Endpoints

### Home Route

GET /

Used to check if the server is running.

---

### Prediction Route

POST /predict

Accepts input data and returns prediction.

---

##  API Testing (Postman)

### Method:

POST

### URL:

http://127.0.0.1:5000/predict

### Body (JSON):

{
"temperature": 85,
"voltage": 230,
"usage_hours": 8,
"vibration": 6,
"humidity": 70
}

---

### Response:

{
"prediction": 1,
"message": "Maintenance Required"
}

---

##  System Flow

Input Data → Flask API → ML Model → Prediction Output

---

##  Use Case

This system can be used in scenarios where monitoring equipment health is important, such as:

* Air conditioning systems
* Industrial machines
* Electrical equipment

---

##  Future Improvements

* Add frontend using React
* Integrate real-world sensor data
* Build dashboard for monitoring
* Support bulk predictions using CSV upload
* Improve model with real datasets

---

##  Notes

* Dataset used here is synthetic (simulated)
* Flask API handles prediction requests
* Postman is used for testing API endpoints

---

##   Conclusion

This project demonstrates the end-to-end workflow of building and deploying a machine learning model for predictive maintenance.
