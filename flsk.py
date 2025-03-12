from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)

model=pickle.load(open('votingS','rb'))

@app.route('/')
def home():
    return render_template('hml.html',prediction_text='')
@app.route('/predict',methods=['POST'])
def predict():

    alcohol=float(request.form['alcohol'])
    malic_acid=float(request.form['malic_acid'])
    ash=float(request.form['ash'])
    alcalinity_of_ash=float(request.form['alcalinity_of_ash'])
    magnesium=float(request.form['magnesium'])
    total_phenols=float(request.form['total_phenols'])
    flavanoids=float(request.form['flavanoids'])
    nonflavanoid_phenols=float(request.form['nonflavanoid_phenols'])
    proanthocyanins=float(request.form['proanthocyanins'])
    color_intensity	=float(request.form['color_intensity'])
    hue	=float(request.form['hue'])
    od315_of_diluted_wines=float(request.form['od280/od315_of_diluted_wines'])
    proline=float(request.form['proline'])
    
    input_data={
        'alcohol':alcohol,
        'malic_acid':malic_acid,
        'ash':ash,
        'alcalinity_of_ash':alcalinity_of_ash,
        'magnesium':magnesium,
        'total_phenols':total_phenols,
        'flavanoids':flavanoids,
        'nonflavanoid_phenols':nonflavanoid_phenols,
        'proanthocyanins':proanthocyanins,
        'color_intensity':color_intensity,
        'hue':hue,
        'od280/od315_of_diluted_wines':od315_of_diluted_wines,
        'proline':proline}
    input_data=pd.DataFrame([input_data])

    prediction=model.predict(input_data)[0]
    Prediction_text=f"Quality: {prediction}"

    return render_template('hml.html',prediction_text=Prediction_text)

if __name__=='__main__':
    app.run(debug=True)
