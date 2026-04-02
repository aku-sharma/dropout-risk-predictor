from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return "API running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    input_data = pd.DataFrame([[
        data['attendance'],
        data['marks'],
        data['backlogs'],
        data['study_hours'],
        data['stress_level']
    ]], columns=['attendance','marks','backlogs','study_hours','stress_level'])

    prediction = model.predict(input_data)[0]

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True, port=5001)