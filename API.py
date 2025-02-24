from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Setup MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sensor_data"]
collection = db["readings"]

@app.route("/data", methods=["POST"])
def save_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    collection.insert_one(data)
    return jsonify({"message": "Data saved"}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
