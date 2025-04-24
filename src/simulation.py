from src import Grid, Hideout, Hunter, Treasure, Knight
import random


class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = Grid(width, height)
        self.hunters = []
        self.knights = []
        self.treasures = []
        self.hideouts = []
        self.initialize_grid()

    def initialize_grid(self):
        pass  # Removed the method to prevent adding extra entities

    def random_position(self):
        return (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

    def add_hunter(self, hunter, x, y):
        if self.grid.place_entity(hunter, x, y):
            self.hunters.append(hunter)
            return True
        return False

    def add_knight(self, knight, x, y):
        if self.grid.place_entity(knight, x, y):
            self.knights.append(knight)
            return True
        return False

    def add_treasure(self, treasure, x, y):
        if self.grid.place_entity(treasure, x, y):
            self.treasures.append(treasure)
            return True
        return False

    def add_hideout(self, hideout, x, y):
        if self.grid.place_entity(hideout, x, y):
            self.hideouts.append(hideout)
            return True
        return False

    def step(self, skip_hunter=None):
        # Process hunter actions
        for hunter in self.hunters:
            if hunter is skip_hunter:
                continue  # Skip user-controlled hunter

            if hunter.stamina > 0:
                nearest_treasure = self._find_nearest_entity(hunter.position, self.treasures)
                nearest_hideout = self._find_nearest_entity(hunter.position, self.hideouts)

                if nearest_treasure and hunter.current_treasure is None:
                    print(f"{hunter.name} at {hunter.position} with stamina {hunter.stamina:.1f} attempting to collect treasure at {nearest_treasure.position}.")
                    if hunter.position == nearest_treasure.position:
                        hunter.collect_treasure(nearest_treasure)
                        if nearest_treasure.collected:
                            self.grid.remove_entity(nearest_treasure)
                            self.treasures.remove(nearest_treasure)
                    else:
                        new_pos = self._move_towards(hunter, nearest_treasure.position)
                        if not self.grid.move_entity(hunter, *new_pos):
                            # If move fails, try alternate paths or skip turn
                            pass
                elif nearest_hideout and hunter.current_treasure:
                    if hunter.position == nearest_hideout.position:
                        hunter.deposit_treasure(nearest_hideout)
                    else:
                        new_pos = self._move_towards(hunter, nearest_hideout.position)
                        if not self.grid.move_entity(hunter, *new_pos):
                            # If move fails, try alternate paths or skip turn
                            pass
            else:
                hunter.rest()

        # Process knight actions
        for knight in self.knights:
            if knight.energy > 0:
                target_hunter = self._find_nearest_entity(knight.position, self.hunters)
                if target_hunter:
                    knight.pursue(target_hunter)
            else:
                knight.rest()

        # Check stopping conditions
        if not self.treasures or all(hunter.stamina <= 0 for hunter in self.hunters):
            print("Simulation ended.")
            return False
        return True

    def _find_nearest_entity(self, position, entities):
        if not entities:
            return None
        px, py = position
        nearest = None
        min_dist = float('inf')
        for entity in entities:
            ex, ey = entity.position
            dist = abs(ex - px) + abs(ey - py)
            if dist < min_dist:
                min_dist = dist
                nearest = entity
        return nearest

    def _move_towards(self, entity, target_pos):
        x, y = entity.position
        tx, ty = target_pos
        dx = 1 if tx > x else -1 if tx < x else 0
        dy = 1 if ty > y else -1 if ty < y else 0
        new_x = x + dx
        new_y = y + dy
        if self.grid.is_within_bounds(new_x, new_y):
            return [new_x, new_y]
        return [x, y]

    def move_active_hunter(self, active_hunter, direction):
        if active_hunter.stamina > 0:
            x, y = active_hunter.position
            if direction == 'up':
                new_pos = (x, y - 1)
            elif direction == 'down':
                new_pos = (x, y + 1)
            elif direction == 'left':
                new_pos = (x - 1, y)
            elif direction == 'right':
                new_pos = (x + 1, y)
            else:
                return  # Invalid direction

            if self.grid.is_within_bounds(*new_pos):
                success, blocker = self.grid.move_entity(active_hunter, *new_pos)
                if not success:
                    print(f"⚠️ Move blocked: space occupied by {blocker}.")
