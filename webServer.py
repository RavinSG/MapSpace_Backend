from flask import Flask, request, session, jsonify
import userCon
import planeGeometry as plane
import sphereGeometry as sphere
import unitConverter as conv
import userDetailsCon as user
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
            "message": "Congratulations, you are an Admin :)",
            "success": True
        }
        return jsonify(msg)


@app.route('/python/get_cords', methods=["POST"])
def show_cords():
    global UNIT_TYPE
    if request.method == "POST":
        print('\n')
        data = json.loads(request.data.decode())
        print(data)
        sGeo = data['sphere']
        cords = data['cords']['val']
        points = convert_to_points(convert)
        if sGeo:
            print('need sgeo')
            area = sphere.calculate_area(points)
        else:
            print(points)
            area = plane.calculate_area(points)
        area = conv.convert_area(area, 'sq.kms', UNIT_TYPE)
        return jsonify(area)


def convert_to_points(coords):
    points = []
    for i in range(len(coords)):
        if i % 2 == 0:
            point = [coords[i]]
        else:
            point.append(coords[i])
            points.append(point)

    return points


@app.route('/python/convert', methods=["POST"])
def convert():
    global UNIT_TYPE
    data = json.loads(request.data.decode())
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    area = data['area']
    return_area = conv.convert_area(area, from_unit, to_unit)
    UNIT_TYPE = to_unit
    return jsonify(return_area)


@app.route('/python/saveArea', methods=["POST"])
def saveArea():
    data = json.loads(request.data.decode())
    points = convert_to_points(data['coordinates']['val'])
    area = conv.convert_area(data['area'], data['unitType'], 'sq.kms')
    user.add_saved_land(area, points, data['center'])
    return jsonify('ok')


if __name__ == "__main__":
    app.run()
