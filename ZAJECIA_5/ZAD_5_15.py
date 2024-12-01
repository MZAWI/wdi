import csv
import math

def create_point_list(csv_file): # creates list of points
    output_points = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)    # skip header
        for row in csv_reader: # create point list
            x, y = row
            output_points.append((float(x), float(y)))
    return output_points

def cos_formula(point1, point2, point3):
    a = math.dist(point2, point3)
    b = math.dist(point1, point2)
    c = math.dist(point1, point3)
    return ((b**2) + (c**2) - (a**2))/(2*b*c)

def is_regular_polygon(csv_points_file, a: float):
    points = create_point_list(csv_points_file)
    print(points)
    closest_points = {}
    for point1 in points:
        value = []
        for point2 in points:
            if math.dist(point1,point2) == a:
                value.append(point2)
        if len(value) != 2:
            return False
        else:
            closest_points[point1] = value

    angles = []
    for point in points:
        angles.append(cos_formula(point,closest_points[point][0],closest_points[point][1]))
    all_same = all(angle == angles[0] for angle in angles)
    if all_same:
        return True
    else:
        return False
    

def main():
    print(is_regular_polygon("figura.csv", 1))


if __name__ == "__main__":
    main()