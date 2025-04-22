import unittest
from mensurapy.perimeter import perimeter

class TestAreaFunction(unittest.TestCase):
    def test_empty_parameter(self):
        self.assertEqual(perimeter(), "Error: No arguments were passed")
        
    def test_1_perimeter_square(self):
        self.assertEqual(perimeter("square", "3m"), "12.0 m")
        
    def test_2_perimeter_square(self):
        self.assertEqual(perimeter("square", "3cm"), "0.12 m")
        
    def test_1_perimeter_rectangle(self):
        self.assertEqual(perimeter("rectangle", "3m", "4m"), "14.0 m")

    def test_2_perimeter_rectangle(self):
        self.assertEqual(perimeter("rectangle", "3cm", "4m"), "8.06 m")
        
    def test_1_perimeter_circle(self):
        self.assertEqual(perimeter("circle", "3m"), "18.84955592153876 m")    

    def test_2_perimeter_circle(self):
        self.assertEqual(perimeter("circle", "3mm"), "0.01884955592153876 m")
        
    def test_1_perimeter_triangle(self):
        self.assertEqual(perimeter("triangle", "4m"), "12.0 m")
        
    def test_2_perimeter_triangle(self):
        self.assertEqual(perimeter("triangle", "4m", "2cm", "4m"), "8.02 m")
        
    def test_3_perimeter_triangle(self):
        self.assertEqual(perimeter("triangle", "4m", "2m"), "10.0 m")
    
    def test_4_perimeter_triangle(self):
        self.assertEqual(perimeter("triangle", "4m", "2cm"), "8.02 m")
        
    def test_perimeter_parallelogram(self):
        self.assertEqual(perimeter("parallelogram", "4cm", "2m"), "4.08 m")
    
    def test_perimeter_rhombus(self):
        self.assertEqual(perimeter("rhombus", "4m"), "16.0 m")
        
    def test_perimeter_trapezium(self):
        self.assertEqual(perimeter("trapezium", "4m", "2m", "4m", "3m"), "13.0 m")
        
    def test_perimeter_ellipse(self):
        self.assertEqual(perimeter("triangle", "4m", "3m"), "11.0 m")    
    

if __name__ == '__main__':
    unittest.main()