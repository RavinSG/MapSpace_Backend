supported_units = ['sq.kms', 'sq.meters', 'sq.miles', 'sq.feet', 'sq.inches', 'Acre', 'Hectare']

ratio_to_sq_inch = {
    'sq.kms': 1550003100.0062,
    'sq.meters': 1550.0031,
    'sq.miles': 4014489600,
    'sq.feet': 144,
    'sq.inches': 1,
    'Acre': 6272640,
    'Hectare': 15500031.000062
}


def convert_area(area, from_unit, to_unit):
    if from_unit not in supported_units or to_unit not in supported_units:
        return "Incorrect units"
    elif area < 0:
        return "Please enter a valid area"
    else:
        converted_area = area * ratio_to_sq_inch[from_unit] / ratio_to_sq_inch[to_unit]

        return converted_area


# print(convert_area(12432,'Acre','sq.miles'))