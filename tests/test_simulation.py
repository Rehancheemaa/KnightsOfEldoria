import unittest
import random
from src.simulation import Simulation  # Corrected import for Simulation class
from src.hunter import Hunter          # Corrected import for Hunter class
from src.knight import Knight          # Corrected import for Knight class
from src.treasure import Treasure      # Corrected import for Treasure class
from src.hideout import Hideout       # Corrected import for Hideout class

class TestSimulation(unittest.TestCase):
    def test_add_entities(self):
        # Create simulation with dynamic size
        grid_size = random.randint(5, 10)
        sim = Simulation(grid_size, grid_size)

        # Create entities with dynamic values
        hunter_stamina = random.randint(3, 8)
        knight_stamina = random.randint(3, 8)
        treasure_value = random.randint(50, 200)
        max_capacity = random.randint(500, 2000)

        hunter = Hunter("Hunter", hunter_stamina)
        knight = Knight("Knight", knight_stamina)
        treasure = Treasure(treasure_value)
        hideout = Hideout("Hide", (0, 0), max_treasure=max_capacity)

        # Add entities at dynamic positions
        hunter_pos = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        knight_pos = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        treasure_pos = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        hideout_pos = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

        sim.add_hunter(hunter, *hunter_pos)
        sim.add_knight(knight, *knight_pos) 
        sim.add_treasure(treasure, *treasure_pos)
        sim.add_hideout(hideout, *hideout_pos)

        # Dynamic assertions to verify entities
        self.assertEqual(len(sim.hunters), 1)
        self.assertEqual(len(sim.knights), 1)
        self.assertEqual(len(sim.treasures), 1)
        self.assertEqual(len(sim.hideouts), 1)

        # Verify entity positions
        self.assertEqual(hunter.position, hunter_pos)
        self.assertEqual(knight.position, knight_pos)
        self.assertEqual(treasure.position, treasure_pos)
        self.assertEqual(hideout.position, hideout_pos)
