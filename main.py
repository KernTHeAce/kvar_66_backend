from flask import Flask
from flask import request, jsonify
from data import OutputJSON
import json
from flask_sock import Sock


app = Flask(__name__)
sock = Sock(app)

data = OutputJSON()

messages = []


@sock.route('/add')
def add(sock):
    while True:
        data = sock.receive()
        messages.append(data)
        sock.send(messages)

@sock.route('/get')
def get(sock):
    while True:
        data = sock.receive()
        sock.send(messages)


@app.route('/')
def index():
    response = jsonify(json.loads(data.to_json()))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/update_Ivan_girls', methods=["POST"])
def update_ivan_girls():
    girls = request.form.get('girls')
    data.Ivan_girl_counter = girls
    return jsonify(isError=False,
                   message="Success",
                   statusCode=200), 200

@app.route("/test", methods=["POST"])
def test():
    data = request.form.get('data')
    messages.append(data)
    return jsonify(isError=False,
                   message="Success",
                   statusCode=200), 200


if __name__ == '__main__':
    app.debug = True
    app.run(host="192.168.62.12", port=5000)  # go to http://localhost:5000/ to view the page.
