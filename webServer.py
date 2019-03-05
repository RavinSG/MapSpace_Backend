from flask import Flask, request
import userCon
import planeGeometry
import landValueCon
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


@app.route('/landvalue', methods=["GET", "POST"])
def landValue():
    if request.method == "GET":
        location = request.args.get('location')
        if location is not None:
            value = landValueCon.get_land_value(location)
            print(value)
            return str(value) + " per Perch"
        else:
            return "Enter Location"

if __name__ == "__main__":
    app.run()
