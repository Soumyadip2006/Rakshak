from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "RAKSHAK",
        "version": "1.0",
        "status": "Running"
    })


if __name__ == "__main__":
    app.run(debug=True)