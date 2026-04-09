from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample crowd data
zones = {
    "Gate A": 50,
    "Food Court": 80,
    "Restroom": 30
}

@app.route("/")
def home():
    return "SmartCrowd AI Running!"

# Get current crowd data
@app.route("/crowd")
def crowd():
    return jsonify(zones)

# Predict crowd (dummy AI logic)
@app.route("/predict")
def predict():
    zone = request.args.get("zone", "Unknown")
    predicted_value = random.randint(10, 120)
    return jsonify({
        "zone": zone,
        "predicted_crowd": predicted_value
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
