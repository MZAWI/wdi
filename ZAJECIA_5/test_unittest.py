import unittest
from ZAD_5_15 import Point, convert_list, forms_regular_polygon_with_free_inside
import math

class TestPoints(unittest.TestCase):
    def test_init(self):
        for x in range(-100,100):
            for y in range(-100,100):
                point = Point((x,y))
                self.assertEqual(point.x, x)
                self.assertEqual(point.y, y)

    def test_point_equality(self):
        for x in range(-100,100):
            for y in range(-100,100):
                point1 = Point((x,y))
                point2 = Point((y,x))
                if x == y:
                    self.assertEqual(point1,point2)
                else:
                    self.assertNotEqual(point1,point2)

    def test_triangle(self): # Triangle
        a = math.sqrt(3) / 2
        point_list = [(0, 0), (1, 0), (0.5, a)]
        self.assertTrue(forms_regular_polygon_with_free_inside(convert_list(point_list)))
    
    def test_square_no_free_inside(self): # Square with occupied inside
        point_list = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
        self.assertFalse(forms_regular_polygon_with_free_inside(convert_list(point_list)))

    def test_square_free_inside(self):
        point_list = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5,1.0001)]
        self.assertTrue(forms_regular_polygon_with_free_inside(convert_list(point_list)))

    def test_minimal_points(self): # Less than 3 points
        point_list = [(0, 0), (1, 0)]
        self.assertFalse(forms_regular_polygon_with_free_inside(convert_list(point_list)))

    def polygon_no_free_inside(self): # Regular hexagon
        r = 1
        point_list = [(r * math.cos(angle), r * math.sin(angle)) 
                      for angle in [i * math.pi / 3 for i in range(6)]]
        self.assertTrue(forms_regular_polygon_with_free_inside(convert_list(point_list)))

if __name__ == '__main__':
    unittest.main()
