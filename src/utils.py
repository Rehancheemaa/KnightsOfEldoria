import math


def calculate_distance(pos1, pos2, grid_width, grid_height, terrain_factor=1.0):
    """
    Calculate the Manhattan distance between two positions with wrap-around logic.
    
    Args:
        pos1: First position tuple
        pos2: Second position tuple 
        grid_width: Width of the grid
        grid_height: Height of the grid
        terrain_factor: Multiplier for distance based on terrain (default 1.0)
    """
    # Ensure both positions are tuples of length 2
    if not all(isinstance(i, tuple) and len(i) == 2 for i in [pos1, pos2]):
        raise ValueError("Both positions must be tuples of length 2.")

    # Calculate wrap-around distances
    dx = min(abs(pos1[0] - pos2[0]), grid_width - abs(pos1[0] - pos2[0]))
    dy = min(abs(pos1[1] - pos2[1]), grid_height - abs(pos1[1] - pos2[1]))
    
    # Apply terrain factor dynamically
    return (dx + dy) * terrain_factor


def stamina_check(entity, action_cost=1.0):
    """
    Check if entity has enough stamina for an action.
    
    Args:
        entity: The entity to check stamina for
        action_cost: Stamina cost multiplier for the action (default 1.0)
    """
    min_stamina = 0.02 * action_cost  # Reflects 2% stamina cost
    
    if entity.stamina <= min_stamina:
        # Calculate recovery time estimate
        recovery_time = (min_stamina - entity.stamina) / entity.stamina_recovery_rate
        print(f"{entity.name} has insufficient stamina! Need {recovery_time:.1f} rest periods to recover.")
        return False
        
    # For entities with sufficient stamina, return true but warn if low
    if entity.stamina < entity.max_stamina * 0.2:
        print(f"Warning: {entity.name}'s stamina is low ({entity.stamina:.1f}/{entity.max_stamina})")
    return True


# Example usage with dynamic terrain
try:
    pos1 = (1, 2)
    pos2 = (4, 6) 
    # Harder terrain increases effective distance
    rough_terrain = 1.5
    distance = calculate_distance(pos1, pos2, 10, 10, rough_terrain)
    print(f"Distance over rough terrain: {distance}")
except ValueError as e:
    print(e)

# Example usage with dynamic stamina costs
try:
    pos1 = (1, 2)
    pos2 = (4,)  # Invalid position
    # Steep terrain increases stamina cost
    steep_terrain = 2.0
    distance = calculate_distance(pos1, pos2, 10, 10)
    print(f"Distance: {distance}")
except ValueError as e:
    print(e)
