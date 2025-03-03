# main.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, Cruel World! Welcome to COC105 CI/CD Lab!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
