import unittest
import random

from .. import point


class TestPointClass(unittest.TestCase):
    def setUp(self):
        pass

    def set_attributes(self):
        x = 3
        y = 9
        test = Point(x, y)
        self.assertEqual(test.x, x)
        self.assertEqual(test.y, y)
        
    def test_coincident(self):
        Point1 = Point(0, 10)
        Point2 = Point(0, 10)
        Point3 = Point(0, 9)
        Point4 = Point(1, 10)
        
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
        marks = ['Blue', 'Rare', 'Medium-Rare', 'Medium', 'Medium-Well', 'Well-Done']
        points = []
        i = 0
        for i in range(20):
            points.append(Point(0, 0, random.choice(marks)))
        
        count = {}
        for i in range(len(points)):
            if points[i].mark in count:
                count[points[i].mark] = count[points[i].mark] + 1
            else:
                count[points[i].mark] = 1 
                
        print (count)
        
        self.assertEqual(count['Rare'], 5)
        self.assertEqual(count['Medium-Well'], 9)
            
            
        
