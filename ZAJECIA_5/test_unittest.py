import unittest
import ZAD_5_15
import math

class TestPoints(unittest.TestCase):
    def test_init(self):
        for x in range(-100,100):
            for y in range(-100,100):
                point = ZAD_5_15.Point((x,y))
                self.assertEqual(point.x, x)
                self.assertEqual(point.y, y)

    def test_point_equality(self):
        for x in range(-100,100):
            for y in range(-100,100):
                point1 = ZAD_5_15.Point((x,y))
                point2 = ZAD_5_15.Point((y,x))
                if x == y:
                    self.assertEqual(point1,point2)
                else:
                    self.assertNotEqual(point1,point2)
            



if __name__ == '__main__':
    unittest.main()
