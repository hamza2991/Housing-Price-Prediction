from gettext import install
from flask import Flask, render_template, request, jsonify
import numpy as np  
import joblib
import json


model= joblib.load("house_model")


with open(r'/home/ubuntu/columns.json' , 'r') as f:
    location = json.load(f)['location']
   



app = Flask(__name__)

@app.route("/")
def welecome():
    return render_template('index.html', loc= location)

@app.route("/submit", methods= ['POST'])
def submit():
    area = float(request.form['area'])
    bhk= float(request.form['bhk'])
    loc_index = location.index (request.form['location'])
    arr = np.array ([[loc_index, area, bhk]])
    return "price is: " +  str (model.predict(arr))

if __name__=='__main__' :
    app.run(host='0.0.0.0', port=8080) 


