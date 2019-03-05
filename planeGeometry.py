def calculate_area(coordinates):
    if len(coordinates) < 3:
        return "At least three points are needed"
    else:
        area = 0
        try:
            for point in range(len(coordinates) - 1):
                area += coordinates[point][0] * coordinates[point + 1][1]
                area -= coordinates[point][1] * coordinates[point + 1][0]

            area += coordinates[0][1] * coordinates[-1][0]
            area -= coordinates[-1][1] * coordinates[0][0]
        except:
            return "Invalid coordinates"

        return abs(area / 2)


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


# points = [[3, 4], [5, 11], [12, 9], [9, 5], [5, 6]]
# check_intersection(points)
# seg = get_segments([[3, 4], [5, 11], [12, 8], [9, 5], [5, 6]])
# print(check_intersection(points))

# solve_equation([2, 2], [4, 1])
# print(point_on_line([0.5, 3], [8, 2]))
