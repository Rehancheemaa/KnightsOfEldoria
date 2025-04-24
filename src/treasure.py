class Treasure:
    def __init__(self, treasure_type, position=None):
        self.treasure_type = treasure_type
        self.position = position
        self.collected = False
        self.value = self.initial_value()
        self.collection_difficulty = 1.0  # Difficulty multiplier for collection
        self.value_multiplier = 1.0  # Dynamic value multiplier

    def initial_value(self):
        if self.treasure_type == 'bronze':
            return 100  # Example initial value
        elif self.treasure_type == 'silver':
            return 200
        elif self.treasure_type == 'gold':
            return 300

    def collect(self):
        """Attempt to collect the treasure with dynamic difficulty and value."""
        if not self.collected:
            # Increase difficulty as value increases
            self.collection_difficulty = 1.0 + (self.value / 1000)
            
            # Adjust value based on collection attempts
            self.value *= self.value_multiplier
            self.value_multiplier = max(0.8, self.value_multiplier * 0.95)
            
            self.collected = True
            return self.value
        return 0

    def decay_value(self):
        if not self.collected:
            self.value *= 0.999  # Decrease by 0.1%
            if self.value <= 0:
                self.value = 0
                self.collected = True

    def update_value(self, nearby_treasures):
        """Dynamically adjust value based on nearby treasures."""
        if not self.collected:
            # Value increases when fewer treasures nearby
            scarcity_bonus = 1.0 + (1.0 / max(1, len(nearby_treasures)))
            self.value *= scarcity_bonus
            
            # Cap maximum value
            self.value = min(self.value, self.value * 2)

    def __str__(self):
        status = "COLLECTED" if self.collected else "AVAILABLE"
        difficulty = f"{self.collection_difficulty:.1f}x"
        value_str = f"{self.value:.0f}" if self.value is not None else "0"
        return f"{self.treasure_type.capitalize()} Treasure at {self.position} | Value: {value_str} | Status: {status} | Difficulty: {difficulty}"
