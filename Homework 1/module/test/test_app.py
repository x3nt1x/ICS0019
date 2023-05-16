import unittest
from src.square_x3nt1x.app import quadratic_formula


class AppTest(unittest.TestCase):
    """Test App"""

    def test_quadratic_formula(self):
        """Check if calculates correctly."""
        self.assertEqual(quadratic_formula(2, 3), 25)
        self.assertEqual(quadratic_formula(-4, -2), 36)


if __name__ == "__main__":
    unittest.main()
