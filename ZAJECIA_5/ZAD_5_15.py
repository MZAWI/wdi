# Class implementation - Remake
# Point format on x,y axis: (x,y)

from math import sqrt

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
        return sqrt(dx**2 + dy**2)
    
    def __eq__(self, other_point): # Define equality
        if isinstance(other_point, Point):
            return (self.x == other_point.x and self.y == other_point.y)
        return False

    # Return list of closest points of the same distance
    # Excluding comparision point
    def closest(self, point_list: list):
        point_list = [point for point in point_list if point != self] # Remove self
        distances = [(point, self.distance(point)) for point in point_list]
        min_distance = min(distances, key = lambda x: x[1])[1]
        closest = [point for point, dist in distances if dist == min_distance]
        return closest
    
    # Check if points from a list can draw equilateral rectangle
def is_equilateral_rectangle(point_list: list):
    if not all(isinstance(point, Point) for point in point_list):
        return False
    if all([len(point.closest(point_list)) == 2 for point in point_list]):
        return True
    return False

def main():
    point_list = [(0,0),(1,1),(1,0),(0,1)]
    point_list = [Point(point) for point in point_list]


    print(is_equilateral_rectangle(point_list))

if __name__ == "__main__":
    main()