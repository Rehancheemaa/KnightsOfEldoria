import random
from .utils import calculate_distance


def move_towards(current, target):
    """Returns a new position one step closer to the target."""
    x, y = current
    tx, ty = target
    dx = 1 if tx > x else -1 if tx < x else 0
    dy = 1 if ty > y else -1 if ty < y else 0
    return [x + dx, y + dy]


def hunter_ai(hunter, grid, treasures, hideouts):
    if hunter.stamina <= 0:
        hunter.rest()
        return

    # If carrying treasure, head to the closest hideout
    if hunter.current_treasure:
        closest_hideout = min(hideouts, key=lambda h: calculate_distance(hunter.position, h.position))
        if hunter.position == closest_hideout.position:
            hunter.deposit_treasure(closest_hideout)
        else:
            hunter.position = move_towards(hunter.position, closest_hideout.position)
            hunter.stamina -= 0.02 * hunter.stamina  # Deplete 2% stamina
        return

    # If not carrying treasure, go for the closest treasure
    if treasures:
        closest = min(treasures, key=lambda t: calculate_distance(hunter.position, t.position))
        if hunter.position == closest.position:
            hunter.collect_treasure(closest)
        else:
            hunter.position = move_towards(hunter.position, closest.position)
            hunter.stamina -= 0.02 * hunter.stamina  # Deplete 2% stamina


def knight_ai(knight, hunters):
    if knight.energy <= 0 or not hunters:
        knight.rest()
        return

    # Prefer hunter with most treasure, otherwise closest
    target = max(hunters, key=lambda h: (h.current_treasure is not None, -calculate_distance(knight.position, h.position)))

    if knight.position != target.position and knight.distance_to(target.position) <= 3:
        knight.position = move_towards(knight.position, target.position)
        knight.energy -= 0.2 * knight.max_energy  # Deplete 20% energy
    elif knight.position == target.position:
        knight.interact_with_hunter(target)
