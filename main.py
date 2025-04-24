import random
from collections import deque
from src.simulation import Simulation
from src.hunter import Hunter
from src.knight import Knight
from src.treasure import Treasure
from src.hideout import Hideout

# === Grid Class Included ===
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}
        self.resize(width, height)

    def resize(self, new_width, new_height):
        old_cells = self.cells.copy()
        self.width = new_width
        self.height = new_height
        self.cells.clear()
        for (x, y), entity in old_cells.items():
            if self.is_within_bounds(x, y):
                self.cells[(x, y)] = entity

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_entity_at(self, x, y):
        return self.cells.get((x, y)) if self.is_within_bounds(x, y) else None

    def place_entity(self, entity, x, y):
        if self.is_within_bounds(x, y) and self.get_entity_at(x, y) is None:
            self.cells[(x, y)] = entity
            entity.position = (x, y)
            return True
        return False

    def move_entity(self, entity, new_x, new_y):
        new_x = new_x % self.width
        new_y = new_y % self.height
        if self.get_entity_at(new_x, new_y) is not None:
            return False
        old_x, old_y = entity.position
        if (old_x, old_y) in self.cells:
            del self.cells[(old_x, old_y)]
            self.cells[(new_x, new_y)] = entity
            entity.position = (new_x, new_y)
            if isinstance(entity, Hunter):
                print(f"{entity.name} moved from ({old_x}, {old_y}) to ({new_x}, {new_y})")
            return True
        return False

    def remove_entity(self, entity):
        x, y = entity.position
        if self.is_within_bounds(x, y) and self.cells.get((x, y)) == entity:
            del self.cells[(x, y)]
            return True
        return False

    def visualize(self):
        print("\n🗺️ Current Grid Map:")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                entity = self.get_entity_at(x, y)
                if entity is None:
                    row += " __ "
                elif isinstance(entity, Hunter):
                    # Show controlled hunter as '🎮' and other hunters as '🏹'
                    if hasattr(entity, 'is_controlled') and entity.is_controlled:
                        row += " 🕵🏻 "
                    else:
                        row += " 🏹 "
                elif isinstance(entity, Knight):
                    row += " 🤺 "
                elif isinstance(entity, Treasure):
                    # Show different icons for different treasure types
                    if entity.treasure_type == "gold":
                        row += " 👑 "
                    elif entity.treasure_type == "silver":
                        row += " 🪙 "
                    elif entity.treasure_type == "diamond":
                        row += " 💎 "
                    elif entity.treasure_type == "bronze":
                        row += " 🥉 "
                    else:
                        row += " 📦 "
                elif isinstance(entity, Hideout):
                    row += " ⛺ "
                else:
                    row += " ? "
            print(row)

# === Pathfinding Utility ===
def find_paths_to_treasures(grid, start, treasures):
    paths = {}
    for treasure in treasures:
        path = bfs_path(grid, start, treasure.position)
        if path:
            paths[treasure] = path
    return paths

def bfs_path(grid, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if grid.is_within_bounds(nx, ny) and (nx, ny) not in visited:
                entity = grid.get_entity_at(nx, ny)
                if entity is None or isinstance(entity, Treasure):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None

# === Simulation Config ===
def configure_simulation():
    print("Welcome to the Eldoria Simulation!")
    while True:
        try:
            grid_size = int(input("Enter grid size (e.g., 20 for a 20x20 grid): "))
            if grid_size < 5:
                print("Grid size must be at least 5x5 for meaningful simulation")
                continue

            max_entities = grid_size * grid_size // 2
            rec_hunters = max(2, grid_size // 4)
            rec_knights = max(1, grid_size // 6)
            rec_treasures = max(5, grid_size // 3)
            rec_hideouts = max(2, grid_size // 5)

            print(f"\nRecommended ranges for {grid_size}x{grid_size} grid:")
            print(f"Hunters: 1-{rec_hunters}")
            print(f"Knights: 1-{rec_knights}")
            print(f"Treasures: 1-{rec_treasures}")
            print(f"Hideouts: 1-{rec_hideouts}")

            num_hunters = int(input("\nEnter number of hunters: "))
            num_knights = int(input("Enter number of knights: "))
            num_treasures = int(input("Enter number of treasures: "))
            num_hideouts = int(input("Enter number of hideouts: "))

            total_entities = num_hunters + num_knights + num_treasures + num_hideouts
            if total_entities > max_entities:
                print(f"Too many entities ({total_entities}) for this grid. Max allowed: {max_entities}")
                continue

            return grid_size, num_hunters, num_knights, num_treasures, num_hideouts
        except ValueError:
            print("Please enter valid numbers.")

# === Main ===
def main():
    try:
        grid_size, num_hunters, num_knights, num_treasures, num_hideouts = configure_simulation()
        sim = Simulation(grid_size, grid_size)
        sim.grid = Grid(grid_size, grid_size)  # Use internal grid

        hunters = []
        for i in range(num_hunters):
            stamina = random.uniform(0.6, 1.0)
            skill = random.choice(["navigation", "stealth", "speed", "strength"])
            hunter = Hunter(f"Hunter-{i+1}", stamina, skill=skill)
            x, y = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
            sim.add_hunter(hunter, x, y)
            hunters.append(hunter)

        for i in range(num_knights):
            energy = random.uniform(0.7, 1.0)
            knight = Knight(f"Knight-{i+1}", energy)
            x, y = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
            sim.add_knight(knight, x, y)

        treasure_types = {
            "bronze": (grid_size * 2, grid_size * 5),
            "silver": (grid_size * 5, grid_size * 10),
            "gold": (grid_size * 10, grid_size * 25),
            "diamond": (grid_size * 25, grid_size * 50)
        }

        for i in range(num_treasures):
            t_type = random.choice(list(treasure_types.keys()))
            value = random.randint(*treasure_types[t_type])
            treasure = Treasure(t_type)
            x, y = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
            sim.add_treasure(treasure, x, y)

        for i in range(num_hideouts):
            capacity = random.randint(grid_size * 100, grid_size * 500)
            hideout = Hideout(f"Hideout-{i+1}", (0, 0), max_treasure=capacity)
            x, y = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
            sim.add_hideout(hideout, x, y)

        controlled_hunter = hunters[0]
        controlled_hunter.is_controlled = True  # Mark the controlled hunter
        print(f"\n🎮 You will control: {controlled_hunter.name} ({controlled_hunter.skill} specialist) 🎮")

        step = 0
        max_steps = grid_size * 10

        while step < max_steps:
            step += 1
            print(f"\n--- Step {step}/{max_steps} ---")

            pos = controlled_hunter.position
            print(f"{controlled_hunter.name} is at {pos} | Stamina: {controlled_hunter.stamina:.2f} | Skill: {controlled_hunter.skill}")

            sim.grid.visualize()

            command = input("Choose action (move [up/down/left/right], rest, status, find treasure): ").strip().lower()

            x, y = pos
            new_pos = None
            if command == "move up":
                new_pos = (x, y - 1)
            elif command == "move down":
                new_pos = (x, y + 1)
            elif command == "move left":
                new_pos = (x - 1, y)
            elif command == "move right":
                new_pos = (x + 1, y)
            elif command == "rest":
                recovery = 0.1 + (0.05 if controlled_hunter.skill == "strength" else 0)
                controlled_hunter.stamina = min(1.0, controlled_hunter.stamina + recovery)
                print(f"{controlled_hunter.name} rests and regains {recovery:.2f} stamina.")
            elif command == "status":
                print(f"Stamina: {controlled_hunter.stamina:.2f}, Skill: {controlled_hunter.skill}")
                print(f"Treasure: {controlled_hunter.current_treasure if controlled_hunter.current_treasure else 'None'}")
            elif command == "find treasure":
                paths = find_paths_to_treasures(sim.grid, controlled_hunter.position, sim.treasures)
                if paths:
                    for treasure, path in paths.items():
                        print(f"Path to {treasure.treasure_type} treasure: {path}")
                else:
                    print("No reachable treasures found.")
            else:
                print("❌ Invalid command.")
                continue

            if new_pos:
                if sim.grid.is_within_bounds(*new_pos):
                    if sim.grid.move_entity(controlled_hunter, *new_pos):
                        stamina_cost = 0.1 * (0.8 if controlled_hunter.skill == "speed" else 1.0)
                        controlled_hunter.stamina = max(0, controlled_hunter.stamina - stamina_cost)
                    else:
                        print("⚠️ Move blocked: space occupied.")
                else:
                    print("⚠️ Move blocked: out of grid bounds.")

            sim.step(skip_hunter=controlled_hunter)

            print("\nHunters Status:")
            for hunter in sim.hunters:
                treasure_status = "💰" if hunter.current_treasure else "—"
                skill_icon = {"navigation": "🧭", "stealth": "👻", "speed": "⚡", "strength": "💪"}[hunter.skill]
                print(f"{hunter.name} at {hunter.position} | Stamina: {hunter.stamina:.2f} | {skill_icon} {hunter.skill} | {treasure_status}")

            print("\nKnights Status:")
            for knight in sim.knights:
                print(f"{knight.name} at {knight.position} | Energy: {knight.energy:.2f}")

            if not sim.treasures:
                print("\n🎉 All treasures collected! Simulation ends.")
                break

        print("\n🏁 Simulation Ended")
        print(f"Total Steps: {step}")
        print(f"Remaining Treasures: {len(sim.treasures)}")
        print("Final Hunter Scores:")
        for hunter in hunters:
            print(f"{hunter.name}: {len(hunter.collected_treasures)} treasures collected")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
