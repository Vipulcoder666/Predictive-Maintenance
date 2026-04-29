# 🔧 Predictive Maintenance System (ML + Flask)

---

# 🎯 Project Goal

The goal of this project is to build a system that can **predict when a machine (like an AC) needs maintenance** using Machine Learning.

👉 Instead of waiting for a machine to fail, the system predicts early based on:

* Temperature
* Voltage
* Usage hours
* Vibration
* Humidity

This helps in:
✔ Reducing sudden failures
✔ Saving cost
✔ Improving efficiency

---

# 🧠 Basic Idea (Simple Understanding)

We are teaching a computer:

👉 “If temperature is high OR usage is high OR voltage is unstable → maintenance required”

This learning is done using a Machine Learning model.

---

# 🔄 Complete Flow of the Project

Step-by-step:

1. We **create data** (simulate sensor data)
2. We **train a model** on that data
3. Model learns patterns
4. We build a **Flask API**
5. User (Postman / app) sends data
6. Model predicts → Maintenance Required or Not

---

# 📁 Project Structure (Very Important)

predictive-maintenance/
│
├── data.py → creates dataset
├── train_model.py → trains ML model
├── visualize.py → shows graph
├── predict.py → manual prediction
├── app.py → Flask API
├── data.csv → generated dataset
├── model.pkl → trained model
└── README.md

---

# 📂 File-by-File Explanation

---

## 🟢 1. data.py

👉 This file creates dataset

What it does:

* Generates random values (like sensors)
* Creates a condition for maintenance

Example logic:

* High temperature
* High usage
* Voltage issue

👉 Output: `data.csv`

---

## 🟡 2. train_model.py

👉 This file trains the model

What it does:

* Loads dataset
* Splits into training & testing
* Trains Random Forest model
* Calculates accuracy
* Saves model

👉 Output: `model.pkl`

---

## 🔵 3. visualize.py

👉 This is for graphs

What it does:

* Shows temperature distribution
* Helps understand data

👉 Used for:
✔ Analysis
✔ Resume value

---

## 🟣 4. predict.py

👉 Manual prediction (without API)

What it does:

* Takes input from keyboard
* Sends to model
* Shows result

👉 Only for understanding (not real system)

---

## 🔴 5. app.py (MOST IMPORTANT)

👉 This is Flask API

What it does:

* Loads trained model
* Creates server
* Accepts input (JSON)
* Returns prediction

👉 This makes project **real-world ready**

---

# ⚙️ Installation

Install required libraries:

pip install pandas numpy scikit-learn matplotlib flask

---

# ▶️ Step-by-Step Execution

---

## 🟢 Step 1: Generate Dataset

python data.py

✔ Creates data.csv

---

## 🟡 Step 2: Train Model

python train_model.py

✔ Shows accuracy
✔ Creates model.pkl

---

## 🔵 Step 3: Visualize (Optional)

python visualize.py

✔ Shows graph

---

## 🟣 Step 4: Run Flask

python app.py

✔ Starts server:

http://127.0.0.1:5000

---

# 🌐 Understanding API Routes

---

## 🟢 Home Route

http://127.0.0.1:5000/

👉 Works in browser
👉 Used to check server

---

## 🔴 Prediction Route

http://127.0.0.1:5000/predict

⚠️ Important:

* Only accepts POST
* Browser sends GET → error

👉 So browser will show:
“Method Not Allowed”

✔ This is correct

---

# 🧪 Postman Testing (IMPORTANT)

---

## Step 1:

Select → POST

---

## Step 2:

Enter URL:

http://127.0.0.1:5000/predict

---

## Step 3:

Go to Body → raw → JSON

---

## Step 4:

Paste:

{
"temperature": 85,
"voltage": 230,
"usage_hours": 8,
"vibration": 6,
"humidity": 70
}

---

## Step 5:

Click Send

---

## ✅ Output:

{
"prediction": 1,
"message": "Maintenance Required"
}

---

# ⚠️ Important Concepts (Very Important)

---

## ❓ Why dataset is used?

👉 Only for training

---

## ❓ Why Postman is used?

👉 To test API

---

## ❓ Why Flask?

👉 To make model usable in real world

---

## ❓ Why browser shows error?

👉 Because:

* Browser → GET
* API → POST

---

# 🔄 System Flow (Final Understanding)

User / Postman / App
↓
Flask API
↓
ML Model
↓
Prediction

---

# 🌍 Real-World Use Case

In real life:

Sensors → API → Model → Dashboard

Example:

* AC sends data automatically
* API predicts
* Alert shown

---

# 🔮 Future Scope (VERY IMPORTANT)

This project can be improved by:

* React frontend (user form)
* Live dashboard
* IoT sensor integration
* Real datasets
* Email alerts
* Mobile app

---

# 💬 Interview Explanation

“I built a predictive maintenance system using Machine Learning. I trained a Random Forest model on sensor data and deployed it using Flask API to provide real-time predictions. The system was tested using Postman and can be integrated with frontend or IoT systems.”

---

# 🔥 Key Highlights

✔ End-to-end ML project
✔ Real-world use case
✔ API deployment
✔ Ready for frontend

---

# 🙌 Final Conclusion

This project shows how a machine learning model can be trained and deployed to solve real-world problems like predicting machine failures before they happen.
