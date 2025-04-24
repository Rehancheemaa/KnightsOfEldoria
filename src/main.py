from simulation import Simulation
from src import Hunter, Knight
from treasure import Treasure
from hideout import Hideout
import random

def configure_simulation():
    print("Welcome to the Eldoria Simulation!")
    grid_size = int(input("Enter grid size (e.g., 20 for a 20x20 grid): "))
    num_hunters = int(input("Enter number of hunters: "))
    num_knights = int(input("Enter number of knights: "))
    num_treasures = int(input("Enter number of treasures: "))
    num_hideouts = int(input("Enter number of hideouts: "))
    return grid_size, num_hunters, num_knights, num_treasures, num_hideouts


def main():
    # Configure simulation parameters
    grid_size, num_hunters, num_knights, num_treasures, num_hideouts = configure_simulation()
    sim = Simulation(grid_size, grid_size)

    # Add hunters
    for _ in range(num_hunters):
        hunter_stamina = random.uniform(0.5, 1.0)
        hunter = Hunter(f"Hunter-{_}", hunter_stamina, skill="navigation")
        sim.add_hunter(hunter, random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    # Add knights
    for _ in range(num_knights):
        knight_energy = random.uniform(0.5, 1.0)
        knight = Knight(f"Knight-{_}", knight_energy)
        sim.add_knight(knight, random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    # Add treasures
    for _ in range(num_treasures):
        treasure_type = random.choice(["bronze", "silver", "gold"])
        treasure = Treasure(treasure_type)
        sim.add_treasure(treasure, random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    # Add hideouts
    for _ in range(num_hideouts):
        hideout = Hideout(f"Hideout-{_}", (0, 0))
        sim.add_hideout(hideout, random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    # Run the simulation
    step = 0
    active_hunter = sim.hunters[0]  # Assuming the first hunter is the active one
    while True:
        step += 1
        print(f"\nStep {step}:")
        if not sim.step(skip_hunter=active_hunter):
            break

        # Detailed status reports
        for hunter in sim.hunters:
            print(f"Hunter {hunter.name} at {hunter.position} with stamina {hunter.stamina:.1f}")
        for knight in sim.knights:
            print(f"Knight {knight.name} at {knight.position} with energy {knight.energy:.1f}")

        # Capture user input for moving the active hunter
        direction = input("Enter direction for active hunter (up, down, left, right): ").strip().lower()
        if direction in ['up', 'down', 'left', 'right']:
            sim.move_active_hunter(active_hunter, direction)
        else:
            print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")

    print("Simulation completed.")


if __name__ == "__main__":
    main()
