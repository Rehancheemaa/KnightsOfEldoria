class Hunter:
    def __init__(self, name, stamina, skill):
        self.name = name
        self.stamina = stamina
        self.skill = skill  # New attribute for hunter's skill
        self.position = (0, 0)
        self.current_treasure = None  # Only one piece of treasure at a time
        self.stamina_recovery_rate = 0.01  # 1% recovery per step

    def collect_treasure(self, treasure):
        print(f"{self.name} attempting to collect treasure at {treasure.position}.")
        if self.stamina <= 0 or self.current_treasure is not None:
            print(f"{self.name} cannot collect treasure: insufficient stamina or already carrying treasure.")
            return False
        if not treasure.collected:
            self.current_treasure = treasure
            treasure.collected = True
            self.stamina -= 0.02 * self.stamina  # Deplete 2% stamina
            print(f"{self.name} collected treasure at {treasure.position}.")
            return True
        print(f"Treasure at {treasure.position} already collected.")
        return False

    def deposit_treasure(self, hideout):
        if self.current_treasure:
            hideout.store_treasure(self.current_treasure.value)
            self.current_treasure = None

    def move_to(self, new_position):
        if self.stamina <= 0:
            return False
        self.position = new_position
        self.stamina -= 0.02 * self.stamina  # Deplete 2% stamina
        return True

    def rest(self):
        if self.stamina < 1.0:
            self.stamina += self.stamina_recovery_rate

    def share_information(self, other_hunters):
        # Placeholder for sharing information logic
        pass

    def recruit_new_hunter(self, hideout):
        # Placeholder for recruitment logic based on skill diversity
        pass

    def __str__(self):
        return f"Hunter {self.name} at {self.position} | Stamina: {self.stamina:.1f} | Skill: {self.skill}"
