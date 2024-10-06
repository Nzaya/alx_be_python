import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, -1), 1)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 3), 0)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(0, 3), 0)
        # Test division by zero
        self.assertIsNone(self.calc.divide(6, 0), "Expected None when dividing by zero")

    def test_edge_cases(self):
        """Additional test cases for edge scenarios."""
        # Large numbers
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.multiply(1e10, 0), 0)
        
        # Small numbers
        self.assertAlmostEqual(self.calc.divide(1e-10, 2), 5e-11)

if __name__ == '__main__':
    unittest.main()
