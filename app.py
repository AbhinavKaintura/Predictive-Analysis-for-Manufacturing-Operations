from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
import joblib
import os

app = Flask(__name__)

# Placeholder for the model and scaler
model = None
scaler = None

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        file_path = os.path.join('dataset', file.filename)
        file.save(file_path)
        return jsonify({"message": "File successfully uploaded"}), 200

@app.route('/train', methods=['POST'])
def train():
    file_path = os.path.join('dataset', 'synthetic_data.csv')  # Change to your file path if different
    if not os.path.exists(file_path):
        return jsonify({"error": "Dataset not found"}), 400
    
    data = pd.read_csv(file_path)
    
    # Assuming the dataset has columns: Machine_ID, Temperature, Run_Time, Downtime_Flag
    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standardize the features
    global scaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize and train the model
    global model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Save the model and scaler
    model_path = os.path.join('models', 'trained_model.pkl')
    scaler_path = os.path.join('models', 'scaler.pkl')
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    
    return jsonify({"accuracy": accuracy, "f1_score": f1}), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({"error": "Model not trained yet"}), 400
    
    data = request.get_json(force=True)
    temperature = data.get('Temperature')
    run_time = data.get('Run_Time')
    
    if temperature is None or run_time is None:
        return jsonify({"error": "Invalid input"}), 400
    
    # Scale the input data
    input_data = [[temperature, run_time]]
    input_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_scaled)
    confidence = model.predict_proba(input_scaled)[0][prediction[0]]
    
    return jsonify({"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": confidence}), 200

if __name__ == '__main__':
    app.run(debug=True)