import math
from ZAD_5_15 import Point, convert_list, forms_regular_polygon_with_free_inside
import pytest

def test_triangle_no_free_inside(): # Triangle
    a = math.sqrt(3) / 2
    point_list = [(0, 0), (1, 0), (0.5, a)]
    assert forms_regular_polygon_with_free_inside(convert_list(point_list)) is True

def test_square_with_inside_occupied():
    point_list = [(0, 0), (1, 0), (1, 1), (0, 1), (0.0001, 0.000001)]
    assert forms_regular_polygon_with_free_inside(convert_list(point_list)) is False

def test_non_regular_polygon():
    point_list = [(0, 0), (1, 0), (0, 1), (1, 1.0001)]
    assert forms_regular_polygon_with_free_inside(convert_list(point_list)) is False

if __name__ == '__main__':
    pytest.main()