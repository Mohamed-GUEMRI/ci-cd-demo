from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        r = requests.get("http://app_b:5001/data")
        return jsonify({"App A": "Got response", "App B": r.json()})
    except:
        return jsonify({"error": "App B not reachable"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
