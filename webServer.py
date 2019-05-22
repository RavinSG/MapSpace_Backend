from flask import Flask, request, session, jsonify
import userCon
import planeGeometry as plane
import sphereGeometry as sphere
import landValueCon
import ast
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(64)

UNIT_TYPE = 'sq.kms'


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
            area = plane.calculate_area(coordinates)
            return str(area) + " sq.Kms"
        elif type == 'sphere':
            return "Still not implemented"
        else:
            return "Select valid type"
    else:
        return "Only post methods are allowed"


@app.route('/python/landvalue', methods=["GET"])
def landValue():
    if request.method == "GET":
        city = request.args.get('city')
        if city is not None:
            value = landValueCon.get_all_values(city)
            print(value)
            return jsonify(value)
        else:
            land_values = landValueCon.get_all_values()
            return jsonify(land_values)


@app.route('/python/login', methods=["POST"])
def login():
    if request.method == "POST":
        data = json.loads(request.data.decode())
        print(data)
        if data != {}:
            username = data['username']
            password = data['password']
            print(username, password)
            if userCon.verify_user(username, password):
                session['username'] = username
                msg = {
                    "success": True,
                    "message": "This is the admin secret"
                }
                return jsonify(msg)
            else:
                msg = {
                    "success": False,
                    "message": "Invalid Credentials"
                }
                return jsonify(msg)
        else:
            if 'username' in session.keys():
                return jsonify({
                    "success": True,
                    "message": "This is the admin secret"
                })
            else:
                return jsonify({
                    "success": False,
                    "message": "Invalid Credentials"
                })


@app.route('/python/logout', methods=["POST"])
def logout():
    if 'username' in session.keys():
        msg = 'logout'
    else:
        msg = 'refresh'
    session.clear()
    return jsonify({
        "message": msg
    })


@app.route('/python/database', methods=["GET"])
def message():
    if request.method == "GET":
        msg = {
            "message": "This is only for admins",
            "success": True
        }
        return jsonify(msg)


@app.route('/python/get_cords', methods=["POST"])
def show_cords():
    if request.method == "POST":
        print('\n')
        data = json.loads(request.data.decode())
        print(data)
        sGeo = data['sphere']
        cords = data['cords']['val']
        points = []
        for i in range(len(cords)):
            if i % 2 == 0:
                point = [cords[i]]
            else:
                point.append(cords[i])
                points.append(point)
        if sGeo:
            print('need sgeo')
            return jsonify(sphere.calculate_area(points))
        else:
            print(points)
            return jsonify(plane.calculate_area(points))


@app.route('/python/get_weather', methods=["GET"])
def show_weather():
    if request.method == "GET":
        return jsonify(data)


data = {
    "message": "",
    "cod": "200",
    "city_id": 2885679,
    "calctime": 0.0823,
    "cnt": 3,
    "list": [{
        "main": {
            "temp": 266.052,
            "temp_min": 266.052,
            "temp_max": 266.052,
            "pressure": 957.86,
            "sea_level": 1039.34,
            "grnd_level": 957.86,
            "humidity": 90},
        "wind": {
            "speed": 1.16,
            "deg": 139.502},
        "clouds": {
            "all": 0
        },
        "weather": [{
            "id": 800,
            "main": "Clear",
            "description": "Sky is Clear",
            "icon": "01n"
        }],
        "dt": 1485722804}, {
        "main": {
            "temp": 263.847,
            "temp_min": 263.847,
            "temp_max": 263.847,
            "pressure": 955.78,
            "sea_level": 1037.43,
            "grnd_level": 955.78,
            "humidity": 91},
        "wind": {
            "speed": 1.49,
            "deg": 159
        },
        "clouds": {
            "all": 0
        },
        "weather": [{
            "id": 800,
            "main": "Clear",
            "description": "Sky is Clear",
            "icon": "01n"}],
        "dt": 1485749608}, {
        "main": {
            "temp": 274.9,
            "pressure": 1019,
            "temp_min": 274.15,
            "temp_max": 275.15,
            "humidity": 88},
        "wind": {
            "speed": 1,
            "deg": 0},
        "clouds": {
            "all": 76},
        "weather": [
            {"id": 500,
             "main": "Rain",
             "description": "light rain",
             "icon": "10d"}],
        "dt": 1485773778
    }]
}

if __name__ == "__main__":
    app.run()
