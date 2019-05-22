from math import sin, cos, radians, asin, acos, sqrt, pi
from pyproj import Proj
from shapely.geometry import shape


def calculate_sphere_area(coordinates):
    lat, lon = zip(*coordinates)

    lat_min = min(lat)
    lat_max = max(lat)
    lat_avg = (lat_min + lat_max) / 2

    lon_avg = sum(lon) / len(lon)

    pa = Proj(f'+proj=aea +lat_1={lat_min} +lat_2={lat_max} +lat_0={lat_avg} +lon_0={lon_avg}')

    x, y = pa(lon, lat)
    cop = {"type": "Polygon", "coordinates": [zip(x, y)]}

    area = shape(cop).area
    print('area', area)
    return area / 10 ** 6


r = 6371


def get_distance(point1, point2):
    lng1, lat1 = point1
    lng2, lat2 = point2
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    dlng = lng2 - lng1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))

    return c * r


def sphere_triangle_area(coordinates):
    point_A = coordinates[0]
    point_B = coordinates[1]
    point_C = coordinates[2]

    a = get_distance(point_A, point_B)
    b = get_distance(point_B, point_C)
    c = get_distance(point_C, point_A)

    # a = b = c = 21.3

    rad_a = a / r
    rad_b = b / r
    rad_c = c / r

    A = acos((cos(rad_a) - cos(rad_b) * cos(rad_c)) / (sin(rad_b) * sin(rad_c)))
    B = acos((cos(rad_b) - cos(rad_a) * cos(rad_c)) / (sin(rad_a) * sin(rad_c)))
    C = acos((cos(rad_c) - cos(rad_b) * cos(rad_a)) / (sin(rad_b) * sin(rad_a)))

    area = (A + B + C - pi) * r ** 2 * 2

    return area


def calculate_area(points):
    area = calculate_sphere_area(points)
    return area
