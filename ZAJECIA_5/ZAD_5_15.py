# Class implementation - Remake
# Point format on x,y axis: (x,y)

import itertools
import math

class Point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def get_coordinates(self):
        return (self.x, self.y)

    def distance(self, other_point): # Calculate distance between two points
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)
    
    def __eq__(self, other_point): # Define equality
        if isinstance(other_point, Point):
            return (self.x == other_point.x and self.y == other_point.y)
        return False
    
    # Return list of closest points of the same distance
    # Excluding comparision point
    def closest(self, point_list: list, tolerance = 1e-9):
        point_list = [point for point in point_list if point != self] # Remove self
        distances = [(point, self.distance(point)) for point in point_list]
        min_distance = min(distances, key = lambda x: x[1])[1]
        return [point for point, dist in distances if abs(dist - min_distance) <= tolerance]
        
    def angle(self, point1, point2): # Find angle between points, where self is middle
        u = Point((point1.x - self.x, point1.y - self.y))
        v = Point((point2.x - self.x, point2.y - self.y))
        dot_product = (u.x * v.x + u.y * v.y)
        u_magnitude = math.sqrt((u.x**2)+(u.y)**2)
        v_magnitude = math.sqrt((v.x**2)+(v.y)**2)

        cos_angle = dot_product / (u_magnitude * v_magnitude)
        return math.acos(cos_angle)
    
# Check if points from a list can draw equilateral polygon
def is_equilateral_polygon(point_list: list):
    if not all(isinstance(point, Point) for point in point_list) or len(point_list) < 3:
        return False
    if all([len(point.closest(point_list)) == 2 for point in point_list]):        
        return True
    return False

# Check if all inside angles are the same 
def same_angles(point_list: list):
    angles = []
    for point in point_list:
        close = point.closest(point_list)
        angles.append(point.angle(close[0],close[1]))
    angles = [round(angle,9) for angle in angles]
    if all(angle == angles[0] for angle in angles):
        return True
    return False

def is_Regular_Polygon(point_list):
    if is_equilateral_polygon(point_list) and same_angles(point_list):
        print(organize_polygon(point_list))
        return True
    return False

def find_regular_polygon(point_list):
    combo = []
    polygons = []
    for i in range(3, len(point_list)+1):
        combo = itertools.combinations(point_list, i)
        for figure in combo:
            # print(figure)
            if is_Regular_Polygon(figure):
                polygons.append(figure)
    return polygons

def find_centroid(point_list: list):
    centroid_x = sum(point.x for point in point_list)/len(point_list)
    centroid_y = sum(point.y for point in point_list)/len(point_list)
    return Point((centroid_x,centroid_y))

def organize_polygon(point_list: list):
    centroid = find_centroid(point_list)

    def centroid_angle(point):
        return math.atan2(point.y - centroid.y, point.x - centroid.x)
    return list(sorted(point_list, key=centroid_angle))

def is_inside_polygon(polygon, point): # Ray casting algorithm
    if point in polygon:
        return False
    polygon = organize_polygon(polygon)
    n = len(polygon)
    if n < 3:
        raise ValueError("There must be at least 3 points")
    count = 0
    for i in range(n):
        current = polygon[i]
        next_point = polygon[(i+1)%n]
        if (current.y > point.y) != (next_point.y > point.y):
            if current.y == next_point.y:
                continue
            x_intersection = (next_point.x - current.x) * (point.y - current.y) / (next_point.y - current.y) + current.x
            if point.x < x_intersection:
                count += 1
    return count % 2 == 1

def forms_regular_polygon_with_free_inside(point_list):
    polygons = find_regular_polygon(point_list)
    for polygon in polygons:
        for point in point_list:
            if is_inside_polygon(polygon, point):
                return False
    return True



def main():
    a = math.sqrt(3)/2
    point_list = [(0,0),(1,1),(0,1),(1,0),(,0.5)]
    point_list = [Point(point) for point in point_list]

    print(forms_regular_polygon_with_free_inside(point_list))

if __name__ == "__main__":
    main()