import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
modelo = pickle.load(open('modelo_regressor.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
	'''
	For rendering results on HTML GUI
	'''
	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction = modelo.predict(final_features)

	output = round(prediction[0],2)

	return render_template('index.html', prediction_text='O peso predito para o peixe é : {}'.format(output))

if __name__ == "__main__":
	app.run(debug=True)
