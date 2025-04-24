class Knight:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.position = (0, 0)
        self.max_energy = energy

    def move_towards(self, target_position):
        x, y = self.position
        tx, ty = target_position
        dx = 1 if tx > x else -1 if tx < x else 0
        dy = 1 if ty > y else -1 if ty < y else 0
        return [x + dx, y + dy]

    def pursue(self, hunter):
        if self.energy <= 0:
            return False
        if self.distance_to(hunter.position) <= 3:
            self.position = self.move_towards(hunter.position)
            self.energy -= 0.2 * self.max_energy  # Deplete 20% energy
            if self.position == hunter.position:
                self.interact_with_hunter(hunter)
            return True
        return False

    def interact_with_hunter(self, hunter):
        if self.energy > 0.2 * self.max_energy:
            # Detain or challenge
            if self.energy > 0.5 * self.max_energy:
                hunter.stamina -= 0.2 * hunter.stamina  # Challenge
            else:
                hunter.stamina -= 0.05 * hunter.stamina  # Detain
            hunter.current_treasure = None

    def rest(self):
        if self.energy < self.max_energy:
            self.energy += 0.1 * self.max_energy  # Recover 10% energy per step

    def distance_to(self, position):
        x, y = self.position
        px, py = position
        return abs(x - px) + abs(y - py)

    def __str__(self):
        return f"Knight {self.name} at {self.position} | Energy: {self.energy:.1f}/{self.max_energy}"
