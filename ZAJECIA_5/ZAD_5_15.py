import csv
import math
import itertools

# Find a cosine of an angle formed by 3 points
# Point 1 is the middle one
def cos_formula(point1, point2, point3):
    a = math.dist(point2, point3)
    b = math.dist(point1, point2)
    c = math.dist(point1, point3)
    return ((b**2) + (c**2) - (a**2))/(2*b*c)

# Check if points from given list form a regular polygon
def is_regular_polygon(points, a: float):
    # print(points)
    closest_points = {}
    # Create a dictionary with one point as value and 
    # two other points with distance a to the point as value
    for point1 in points: 
        value = []
        for point2 in points:
            if round(math.dist(point1,point2),4) == a:
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
    
def any_regular_polygons(points, a):
    combo = []
    for i in range(3, len(points)+1):
        combo = itertools.combinations(points, i)
        for figure in combo:
            # print(figure)
            if is_regular_polygon(figure, a):
                return True
    return False
        
def main():
    figura = [(0,0),(0,1),(1,0),(0,12),(1,1)]
    # figura - 
    print(any_regular_polygons(figura, 1))

if __name__ == "__main__":
    main()