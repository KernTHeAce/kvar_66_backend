from flask import Flask
from flask import request, jsonify
from data import OutputJSON

app = Flask(__name__)

data = OutputJSON()


@app.route('/')
def index():
    return data.to_json()


@app.route('/update_Ivan_girls', methods=["POST"])
def update_ivan_girls():
    girls = request.form.get('girls')
    data.Ivan_girl_counter = girls
    return jsonify(isError=False,
                   message="Success",
                   statusCode=200), 200


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.
