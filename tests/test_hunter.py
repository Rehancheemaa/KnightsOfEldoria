import unittest
import random
from src.hunter import Hunter         # Corrected import for Hunter class
from src.treasure import Treasure     # Corrected import for Treasure class
from src.hideout import Hideout      # Corrected import for Hideout class

class TestHunter(unittest.TestCase):
    def test_collect_treasure(self):
        # Create instances with dynamic values
        stamina = random.randint(3, 8)
        treasure_value = random.randint(50, 200)
        hunter = Hunter("Test", stamina)
        treasure = Treasure(treasure_value)

        # Test collection with dynamic difficulty
        initial_stamina = hunter.stamina
        hunter.collect_treasure(treasure)

        # Assert dynamic collection results
        self.assertEqual(hunter.collected_treasure, treasure_value)
        self.assertTrue(treasure.collected)
        self.assertLess(hunter.stamina, initial_stamina)  # Verify stamina cost
        self.assertGreaterEqual(hunter.collection_efficiency, 0.5)

    def test_deposit_treasure(self):
        # Create instances with dynamic capacities
        stamina = random.randint(3, 8)
        max_capacity = random.randint(500, 2000)
        hunter = Hunter("Test", stamina)
        hideout = Hideout("Base", (0, 0), max_treasure=max_capacity)

        # Test deposits with varying amounts
        test_amounts = [random.randint(50, 200) for _ in range(3)]
        for amount in test_amounts:
            hunter.collected_treasure = amount
            initial_stamina = hunter.stamina
            hunter.deposit_treasure(hideout)

            # Assert dynamic deposit results
            self.assertEqual(hideout.stored_treasure, amount)
            self.assertEqual(hunter.collected_treasure, 0)
            self.assertLess(hunter.stamina, initial_stamina)  # Verify stamina cost
            self.assertLessEqual(hideout.stored_treasure, hideout.max_treasure)
