# 🚦 Traffic Forecasting and Classification using LSTM & Logistic Regression

This project delivers a hybrid solution for **traffic volume forecasting** and **congestion classification** using **LSTM** and **Logistic Regression** models. The application is powered by a custom-built **HTML + CSS frontend**, offering a clean and interactive user interface for end-users to visualize predictions and classifications in real time.

---

## 📌 Key Features

- 🧠 **LSTM** model to forecast future traffic volume based on historical patterns
- 📊 **Logistic Regression** to classify traffic conditions (e.g., Low, Moderate, High)
- 🌐 Interactive frontend built using **HTML and CSS**
- 📈 Visual display of prediction results and traffic category
- 📤 Option to input/upload test data directly through the interface

---

## 🧠 Models Used

### 🔮 LSTM – Time Series Forecasting
- Framework: TensorFlow/Keras
- Trained on sequential traffic data to predict future volume
- Optimized using MSE loss and early stopping

### ⚙️ Logistic Regression – Classification
- Classifies traffic into:
  - 🟢 Low Traffic
  - 🟡 Moderate Traffic
  - 🔴 High Traffic
- Uses features like time, weather, day of week, and volume metrics

---

## 🖥️ Front-End Preview

![Screenshot 2025-04-15 211035](https://github.com/user-attachments/assets/d2315e43-0a2b-4440-9794-ca07b21419bf)

![Screenshot 2025-04-15 211053](https://github.com/user-attachments/assets/6e97c8d9-64ba-4938-881f-2d3aa06231fc)

----

## 🗂️ Project Structure

traffic-forecasting-lstm-logistic/
├── models/
│   ├── lstm_model.h5
│   └── logistic_model.pkl
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py                    # Backend logic (Flask/FastAPI if used)
├── data/
│   └── traffic_data.csv
├── README.md
└── requirements.txt

## 📊 Sample Outputs
Predicted Traffic Volume: 1234 vehicles/hour

Traffic Category: 🟡 Moderate

Line chart of actual vs. predicted volume

Classification summary for the next N time steps



