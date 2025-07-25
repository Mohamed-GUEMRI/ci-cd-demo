from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data")
def get_data():
    return jsonify({"message": "Hello from App B!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
