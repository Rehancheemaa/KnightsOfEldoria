import unittest
import random
from src.knight import Knight      # Corrected import for Knight class
from src.hunter import Hunter      # Corrected import for Hunter class

class TestKnight(unittest.TestCase):
    def test_chase(self):
        # Create instances with dynamic values
        knight_stamina = random.randint(3, 8)
        hunter_stamina = random.randint(2, 6)
        knight = Knight("Guard", knight_stamina)
        hunter = Hunter("Thief", hunter_stamina)

        # Set dynamic test conditions
        treasure_amount = random.randint(50, 200)
        hunter.collected_treasure = treasure_amount
        
        # Record initial positions and stats
        initial_knight_stamina = knight.stamina
        initial_hunter_stamina = hunter.stamina

        # Knight chases the hunter
        knight.chase(hunter)

        # Assert chase results with dynamic values
        self.assertEqual(knight.position, hunter.position)
        self.assertEqual(hunter.collected_treasure, 0)
        
        # Verify stamina costs
        self.assertLess(knight.stamina, initial_knight_stamina)
        self.assertLess(hunter.stamina, initial_hunter_stamina)
        
        # Test chase effectiveness
        self.assertGreaterEqual(knight.chase_success_rate, 0.5)
