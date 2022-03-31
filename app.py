
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
crop_recommendation_model_path = 'model.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))
 

@app.route('/')
def home():
    return render_template('index00.html')

@app.route('/predict',methods=['POST'])
def predict():
 


    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['Pottasium'])
        Temperature = int(request.form['Temperature'])
        Rainfall = int(request.form['Rainfall'])
        Humidity = int(request.form['Humidity'])
        ph = float(request.form['ph'])
        

        
        
    data =  np.array([[N, P, K, Temperature, Rainfall, Humidity, ph]])
    my_prediction = crop_recommendation_model.predict(data)
    final_prediction = my_prediction[0]

            

    return render_template('index00.html', prediction= final_prediction)

        


     

    

if __name__ == "__main__":
    app.run(debug=True, port=8000)

