import unittest
import numpy as np
import sys

# Add /app to path so we can import the AI's solution
sys.path.append('/app')

try:
    from grid_transform import solve
except ImportError:
    solve = None

class TestGridTransform(unittest.TestCase):
    def test_import(self):
        """Check if function exists."""
        self.assertIsNotNone(solve, "Could not import 'solve' from grid_transform.py")

    def test_example_case(self):
        """Verify the example provided in the prompt."""
        input_grid = [[8, 6], [6, 4]]
        expected = [
            [8, 6, 8, 6, 8, 6],
            [6, 4, 6, 4, 6, 4],
            [6, 8, 6, 8, 6, 8],  # Flipped row 0
            [4, 6, 4, 6, 4, 6],  # Flipped row 1
            [8, 6, 8, 6, 8, 6],
            [6, 4, 6, 4, 6, 4]
        ]
        result = solve(input_grid)
        np.testing.assert_array_equal(result, expected)

    def test_generalization(self):
        """Test with new numbers to ensure no hardcoding."""
        input_grid = [[1, 2], [3, 4]]
        expected = [
            [1, 2, 1, 2, 1, 2],
            [3, 4, 3, 4, 3, 4],
            [2, 1, 2, 1, 2, 1],  # Flipped: 1,2 -> 2,1
            [4, 3, 4, 3, 4, 3],  # Flipped: 3,4 -> 4,3
            [1, 2, 1, 2, 1, 2],
            [3, 4, 3, 4, 3, 4]
        ]
        result = solve(input_grid)
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()