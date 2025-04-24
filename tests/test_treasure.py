import unittest
import random
from src.treasure import Treasure   # Corrected import for Treasure class

class TestTreasure(unittest.TestCase):
    def test_initial_state(self):
        # Create a treasure object with dynamic value
        treasure_value = random.randint(50, 500)
        treasure = Treasure(treasure_value)

        # Assert that the value matches the random value
        self.assertEqual(treasure.value, treasure_value)

        # Assert that the treasure is not collected initially
        self.assertFalse(treasure.collected)
