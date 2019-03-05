from flask import Flask, request, flash
import userCon
import planeGeometry
import ast

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        userCon.add_user(username, password)
    return "not post"


@app.route('/calcarea', methods=["POST"])
def calculateArea():
    if request.method == "POST":
        type = request.form['type']
        coordinates = request.form['coordinates']
        coordinates = ast.literal_eval(coordinates)
        if type == 'plane':
            area = planeGeometry.calculate_area(coordinates)
            return str(area) + " sq.Kms"
        elif type == 'sphere':
            return "Still not implemented"
        else:
            return "Select valid type"
    else:
        return "Only post methods are allowed"


if __name__ == "__main__":
    app.run()
