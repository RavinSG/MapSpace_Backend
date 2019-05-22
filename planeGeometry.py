import math


def calculate_area(coordinates):
    if len(coordinates) == 2:
        alpha = get_alpha(coordinates[0][0])
        dist = (coordinates[0][0] - coordinates[1][0]) ** 2 + (coordinates[0][1] - coordinates[1][1]) ** 2
        dist = dist ** 0.5
        return dist * alpha

    elif len(coordinates) < 3:
        return "At least three points are needed"

    else:
        area = 0
        alpha = get_alpha(coordinates[0][0])
        print('alpha - ', alpha)
        try:
            for point in range(len(coordinates) - 1):
                area += coordinates[point][0] * coordinates[point + 1][1]
                area -= coordinates[point][1] * coordinates[point + 1][0]

            area += coordinates[0][1] * coordinates[-1][0]
            area -= coordinates[-1][1] * coordinates[0][0]
        except:
            return "Invalid coordinates"

        true_area = area * alpha ** 2 / 2

        return abs(true_area)


def get_alpha(lng):
    degree = lng // 1 + (lng % 1) * 60
    radian = degree * math.pi / 180
    alpha = 111 * math.cos(radian)

    return alpha


def get_segments(coordinates):
    coordinates.append(coordinates[0])
    segments = []
    for point in range(len(coordinates) - 1):
        segments.append([coordinates[point], coordinates[point + 1]])
    return segments


def get_line_equation(segment):
    point_a = segment[0]
    point_b = segment[1]

    m = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])
    c = point_a[1] - point_a[0] * m
    return [m, c]


def solve_equation(line1, line2):
    x = - (line1[1] - line2[1]) / (line1[0] - line2[0])
    y = line1[0] * x + line1[1]
    print(x, y)


def point_on_line(point, line_equation):
    x = point[0]
    y = point[1]
    m = line_equation[0]
    c = line_equation[1]

    if y == (m * x + c):
        return True
    else:
        return False


def check_intersection(coordinates):
    segments = get_segments(coordinates)
    line_equations = []
    for segment in segments:
        line_equations.append(get_line_equation(segment))

    for i in range(len(line_equations) - 2):
        intersections = []
        line = line_equations[i]
        for j in range(i + 2, len(line_equations)):
            intersections.append(solve_equation(line, line_equations[j]))
        print(intersections)

    return line_equations


def get_t_value(line1, line2):
    p1, p2 = line1
    p3, p4 = line2

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x1)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    print(t)


# get_t_value([[-5, 0], [0, 4]], [[5, 0], [0, 0]])
