import unittest
from mensurapy.area import area

class TestAreaFunction(unittest.TestCase):
    def test_empty_parameter(self):
        self.assertEqual(area("square", "3m"), "9.0 m²")

    """
    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)
    """

if __name__ == '__main__':
    unittest.main()
