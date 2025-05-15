
import unittest
from geometry.shapes import Circle, Triangle, ShapeFactory

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), 3.141592653589793)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_shape_factory_circle(self):
        shape = ShapeFactory.create_shape('circle', 2)
        self.assertIsInstance(shape, Circle)

    def test_shape_factory_triangle(self):
        shape = ShapeFactory.create_shape('triangle', 3, 4, 5)
        self.assertIsInstance(shape, Triangle)

