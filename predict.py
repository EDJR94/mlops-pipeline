# predict.py
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model (in production, load from a mounted volume or GCS)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
