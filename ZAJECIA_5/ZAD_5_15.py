import csv
import math

# Reads list of points from csv file
def create_point_list(csv_file):
    output_points = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)    # skip header
        for row in csv_reader: # create point list
            x, y = row
            output_points.append((float(x), float(y)))
    return output_points

# Find a cosine of an angle formed by 3 points
# Point 1 is the middle one
def cos_formula(point1, point2, point3):
    a = math.dist(point2, point3)
    b = math.dist(point1, point2)
    c = math.dist(point1, point3)
    return ((b**2) + (c**2) - (a**2))/(2*b*c)

# Check if points from given list form a regular polygon
def is_regular_polygon(csv_points_file, a: float):
    points = create_point_list(csv_points_file)
    print(points)
    closest_points = {}
    # Create a dictionary with one point as value and 
    # two other points with distance a to the point as value
    for point1 in points: 
        value = []
        for point2 in points:
            if math.dist(point1,point2) == a:
                value.append(point2)
        # Return false if there are not exactly 2 points 
        # with distance a to the point
        if len(value) != 2:
            return False
        else:
            closest_points[point1] = value
    angles = []
    for point in points: # Check if all internal angles are the same
        angles.append(cos_formula(point,closest_points[point][0],closest_points[point][1]))
    for i in range(len(angles)):
        angles[i] = round(angles[i], 6) # round the values to avoid errors
    all_same = all(angle == angles[0] for angle in angles)
    if all_same:
        return True
    else:
        return False

def main():
    print(is_regular_polygon("figura.csv", 1))

if __name__ == "__main__":
    main()