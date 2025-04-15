import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle
from flask import Flask, flash, request, redirect, url_for, render_template
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__) #Initialize the flask App
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# === LOAD MODEL =====
model_path = r"C:\Users\njhar\Documents\automatic road traffic control\Batch-6(Automatic_Road_Traffic_Verifictaion_System)\Traffic_forecast_07.03.2023\linear_regression_model.pkl"
model = pickle.load(open(model_path, 'rb'))


# === INDEX PAGE =====

@app.route('/')
@app.route('/')
@app.route('/index')

def index():
	return render_template('index.html')

# === LOGIN PAGE =====

@app.route('/login') 
def login():
    return render_template('index1.html') 

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        junction = int(request.form['junction'])
        ID = int(request.form['ID'])

        values = np.array([[junction, ID]])
        prediction = model.predict(values)

        return render_template('result.html', prediction=prediction)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)