import unittest
from src.hideout import Hideout  # Corrected import path to src.hideout

class TestHideout(unittest.TestCase):
    def test_store_treasure(self):
        # Create a Hideout instance with dynamic capacity
        max_capacity = 1000
        hideout = Hideout("Cave", (0, 0), max_treasure=max_capacity)

        # Test storing different amounts of treasure
        test_amounts = [50, 150, 300]
        total = 0
        
        for amount in test_amounts:
            hideout.store_treasure(amount)
            total += amount
            self.assertEqual(hideout.stored_treasure, total)
            self.assertLessEqual(hideout.stored_treasure, max_capacity)

        # Test storing beyond capacity
        with self.assertRaises(ValueError):
            hideout.store_treasure(max_capacity + 1)

        # Test dynamic storage efficiency
        self.assertGreaterEqual(hideout.storage_efficiency, 0.5)
        self.assertLessEqual(hideout.storage_efficiency, 1.0)
