import unittest
import random

from .. import Point


class TestPointClass(unittest.TestCase):
    def setUp(self):
        pass

    def set_attributes(self, x, y):
        test = Point(x, y)
        self.assertEqual(test.x, x)
        self.assertEqual(test.y, y)
        
    def test_coincident(self):
        Point1 = (0, 10)
        Point2 = (0, 10)
        Point3 = (0, 9)
        Point4 = (1, 10)
        
        self.assertTrue(Point1.check_coincident(Point2))
        self.assertFalse(Point1.check_coincident(Point3))
        self.assertFalse(Point1.check_coinsident(Point4))
    
    def test_shift(self):
        test = Point(0, 10)
        test.shift_point(5, 5)
        
        self.assertEqual(test.x, 5)
        self.assertEqual(test.y, 15)
        
    def test_marked_points(self):
        random.seed(12345)
        marks = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
        points = []
        i = 0
