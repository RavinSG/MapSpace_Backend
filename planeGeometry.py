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
    return m, c


def check_intersection(coordinates):
    segments = get_segments(coordinates)
    line_equations = []
    for segment in segments:
        print(segment)
        line_equations.append(get_line_equation(segment))

    return line_equations


points = [[3, 4], [5, 11], [12, 8], [9, 5], [5, 6]]
# seg = get_segments([[3, 4], [5, 11], [12, 8], [9, 5], [5, 6]])
print(check_intersection(points))
