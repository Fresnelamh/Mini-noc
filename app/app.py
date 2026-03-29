from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "App is running"})

@app.route("/data")
def data():
    return jsonify({"users": 42, "requests_today": 1337})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)