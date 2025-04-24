class Hideout:
    def __init__(self, name, position, max_treasure=1000, max_hunters=5):
        self.name = name
        self.position = position
        self.stored_treasure = 0
        self.max_treasure = max_treasure
        self.hunters = []  # List to manage hunters in the hideout
        self.max_hunters = max_hunters
        self.is_full = False
        self.storage_rate = 1.0  # Storage efficiency multiplier

    def store_treasure(self, value):
        """Store treasure in the hideout dynamically based on capacity and storage rate."""
        effective_value = value * self.storage_rate
        available_space = self.max_treasure - self.stored_treasure
        
        if available_space >= effective_value:
            self.stored_treasure += effective_value
            if self.stored_treasure >= self.max_treasure * 0.9:  # 90% full
                self.storage_rate *= 0.8  # Reduce storage efficiency
                self.is_full = True
            return effective_value
        else:
            stored = available_space
            self.stored_treasure = self.max_treasure
            self.is_full = True
            self.storage_rate *= 0.5  # Significantly reduce storage rate when full
            return stored

    def retrieve_treasure(self, value):
        """Retrieve treasure dynamically with variable rates based on stored amount."""
        if self.stored_treasure >= value:
            self.stored_treasure -= value
            if self.stored_treasure < self.max_treasure * 0.7:  # Below 70%
                self.storage_rate = min(1.0, self.storage_rate * 1.2)  # Improve rate
                self.is_full = False
            return value
        else:
            available = self.stored_treasure
            self.stored_treasure = 0
            self.storage_rate = 1.0  # Reset storage rate when empty
            self.is_full = False
            return available

    def add_hunter(self, hunter):
        if len(self.hunters) < self.max_hunters:
            self.hunters.append(hunter)
            return True
        return False

    def remove_hunter(self, hunter):
        if hunter in self.hunters:
            self.hunters.remove(hunter)
            return True
        return False

    def share_information(self):
        # Placeholder for logic to share information among hunters
        pass

    def __str__(self):
        """Enhanced string representation with dynamic status."""
        status = "FULL" if self.is_full else "AVAILABLE"
        efficiency = f"{self.storage_rate:.1%}"
        return f"Hideout {self.name} at {self.position} | Status: {status} | Storage: {self.stored_treasure}/{self.max_treasure} | Efficiency: {efficiency} | Hunters: {len(self.hunters)}/{self.max_hunters}"
