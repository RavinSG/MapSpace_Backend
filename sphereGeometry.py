from math import sin, cos, radians, asin, acos, sqrt, pi

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


print(sphere_triangle_area([[27.807886, 88.204596], [30.232151, 81.337642], [28.824699, 80.081678]]))
