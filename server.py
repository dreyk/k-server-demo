#!flask/bin/python
from flask import Flask, jsonify

print("Running Kuberlab server\n")

app = Flask(__name__)

counter = 0

@app.route('/stats/counter', methods=['GET'])
def get_counter():
    global counter
    counter += 1
    return jsonify({'counter': counter})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
