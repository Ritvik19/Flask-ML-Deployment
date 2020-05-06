import numpy as np
from flask import Flask, request, jsonify, render_template
from app import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    inp = str(list(request.form.values())[0])
    features = generateFeatures(inp)
    prediction = getPredictions(features)

    return render_template('index.html', inp=inp, prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)