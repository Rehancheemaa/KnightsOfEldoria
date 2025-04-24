class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}  # Using dictionary for sparse storage
        self.resize(width, height)

    def resize(self, new_width, new_height):
        """Dynamically resize the grid while preserving entities"""
        old_cells = self.cells.copy()
        self.width = new_width
        self.height = new_height
        self.cells.clear()
        
        # Only keep entities that would still be within bounds
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
        # Wrap around the grid edges
        new_x = new_x % self.width
        new_y = new_y % self.height

        target_entity = self.get_entity_at(new_x, new_y)
        if target_entity is not None and not isinstance(target_entity, Treasure):
            entity_name = getattr(target_entity, 'name', 'unknown')
            return False, f"{type(target_entity).__name__} ({entity_name})"  # Return the type and name of the blocking entity

        old_x, old_y = entity.position
        if (old_x, old_y) in self.cells:
            del self.cells[(old_x, old_y)]
        self.cells[(new_x, new_y)] = entity
        entity.position = (new_x, new_y)

        # If the target entity is a treasure, collect it
        if isinstance(target_entity, Treasure):
            entity.collect_treasure(target_entity)
            return True, None  # Return None when move is successful and treasure is collected

        return True, None  # Return None when move is successful

    def remove_entity(self, entity):
        x, y = entity.position
        if self.is_within_bounds(x, y) and self.cells.get((x, y)) == entity:
            del self.cells[(x, y)]
            return True
        return False

    def __str__(self):
        display = ""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                entity = self.get_entity_at(x, y)
                row.append("." if entity is None else str(entity)[0])
            display += " ".join(row) + "\n"
        return display
