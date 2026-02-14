from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app) # Necessary for the HTML test to work

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = data.get('features')
        model_path = data.get('model_path') # This will be 'my_model.pkl'
        
        # Load the model we just created
        model = joblib.load(model_path)
        
        # Features should be a list like [5.1, 3.5, 1.4, 0.2]
        prediction = model.predict([features]) 
        
        return jsonify({
            'prediction': prediction.tolist(),
            'label': 'Sentosa/Versicolor/Virginica' # Iris category
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)