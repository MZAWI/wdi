# Class implementation - Remake
# Point format on x,y axis: (x,y)

import math

class Point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def get_coordinates(self):
        return (self.x, self.y)

    # Calculate distance between two points
    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return round(math.sqrt(dx**2 + dy**2),6)

    # Check if two points are the same
    def isEqual(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True
        return False

# Return list of the closest points of the same distance to the given point
def closest_points(base: Point, points: list):
    # Remove base from points list if present
    points = [point for point in points if not base.isEqual(point)]

    # Prepare list of distances between point1 and other points
    distances = [(point, base.distance(point)) for point in points]
    # Find the minimum distance 
    min_distance = min(distances, key = lambda x: x[1])
    closest = []
    for distance in distances:
        if distance[1] == min_distance[1]:
            closest.append(min_distance[0])
    return(closest)

def main():
    point_list = [(0,0),(1,1),(2,2),(1,0)]
    for i in range(len(point_list)):
        point_list[i] = Point(point_list[i])
    print(point_list)

    print(closest_points(Point((0,0)),point_list))

if __name__ == "__main__":
    main()