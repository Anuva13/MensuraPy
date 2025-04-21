import unittest
from mensurapy.area import area

class TestAreaFunction(unittest.TestCase):
    def test_empty_parameter(self):
        self.assertEqual(area(), "Error: No arguments were passed")
    
    def test_wrong_shape(self):
        self.assertEqual(area("trapezoid", "10m", "6m", "5m"), "Error in parameter parsing: cannot unpack non-iterable NoneType object")    
        
    def test_area_square(self):
        self.assertEqual(area("square", "3m"), "9.0 m²")
        
    def test_area_rectangle1(self):
        self.assertEqual(area("rectangle", "3cm", "5cm"), "0.0015 m²")
        
    def test_area_rectangle2(self):
        self.assertEqual(area("rectangle", "3m", "5m"), "15.0 m²")
        
    def test_area_circle(self):
        self.assertEqual(area("circle", "3m"), "28.274333882308138 m²")
        
    def test_area_equilateral_triangle(self):
        self.assertEqual(area("triangle", "2m"), "1.7320508075688772 m²")
        
    def test_area_scalene_triangle(self):
        self.assertEqual(area("triangle", "2m", "3cm", "30degrees"), "0.014999999999999998 m²")
        
    def test_area_right_triangle(self):
        self.assertEqual(area("triangle", "3m", "400cm"), "6.0 m²")
        
    def test_area_triangle(self):
        self.assertEqual(area("triangle", "1.2m", "85cm", "0.00095km"), "0.4010922587136282 m²")
    
    def test_1_area_parallelogram(self):
        self.assertEqual(area("parallelogram", "10m", "6m"), "60.0 m²")
    
    def test_2_area_parallelogram(self):
        self.assertEqual(area("parallelogram", "8m", "5m", "60degrees"), "34.64101615137754 m²")
        
    def test_3_area_parallelogram(self):
        self.assertEqual(area("parallelogram", "8m", "5000mm", "60degrees"), "34.64101615137754 m²")

    def test_1_area_rhombus(self):
        self.assertEqual(area("rhombus", "8m", "6m"), "24.0 m²")
        
    def test_2_area_rhombus(self):
        self.assertEqual(area("rhombus", "800cm", "6m"), "24.0 m²")
        
    def test_1_area_trapezium(self):
        self.assertEqual(area("trapezium", "10m", "6m", "5m"), "40.0 m²")
        
    def test_2_area_trapezium(self):
        self.assertEqual(area("trapezium", "1000cm", "6m", "500cm"), "40.0 m²")
        
    def test_3_area_trapezium(self):
        self.assertEqual(area("trapezium", "8m", "4m", "6m", "60degrees"), "31.17691453623979 m²")
        
    def test_4_area_trapezium(self):
        self.assertEqual(area("trapezium", "8m", "400cm", "6m", "60degrees"), "31.17691453623979 m²")

    def test_5_area_trapezium(self):
        self.assertEqual(area("trapezium", "60degrees", "8m", "400cm", "6m"), "31.17691453623979 m²")

    def test_area_ellipse(self):
        self.assertEqual(area("ellipse", "5m", "3m"), "47.12388980384689 m²")

if __name__ == '__main__':
    unittest.main()
