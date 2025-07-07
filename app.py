from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model and column names
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.zeros(len(columns))

    for key, value in data.items():
        if key in columns:
            index = columns.index(key)
            input_data[index] = value

    prediction = model.predict([input_data])[0]
    return jsonify({'predicted_price': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True, port=5050)

