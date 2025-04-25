# Knights of Eldoria - Project Report

## Project Overview
Knights of Eldoria is an interactive simulation game that features knights and treasure hunters in a dynamic grid-based world. The game combines elements of strategy, resource management, and tactical decision-making in a medieval fantasy setting.

## Project Structure
```
KnightsOfEldoria/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── simulation.py
│   ├── grid.py
│   ├── hunter.py
│   ├── knight.py
│   ├── treasure.py
│   ├── hideout.py
│   ├── utils.py
│   └── ai_agents.py
├── tests/
│   ├── test_treasure.py
│   ├── test_simulation.py
│   ├── test_knight.py
│   ├── test_hunter.py
│   └── test_hideout.py
├── setup.py
└── requirements.txt
```

## Core Components

### 1. Grid System
- Implements a flexible grid-based world
- Supports dynamic resizing
- Handles entity placement and movement
- Provides visualization with emoji-based representation

### 2. Entities

#### Hunters
- Specialized hunters with unique skills:
  - Navigation (🧭)
  - Stealth (👻)
  - Speed (⚡)
  - Strength (💪)
- Stamina-based movement system
- Treasure collection capabilities

#### Knights
- Energy-based movement system
- Defensive role in the simulation
- Unique positioning and behavior patterns

#### Treasures
- Multiple types with varying values:
  - Bronze (🥉)
  - Silver (🪙)
  - Gold (👑)
  - Diamond (💎)
- Value scaling based on grid size

#### Hideouts
- Safe zones for treasure storage
- Capacity-based storage system
- Strategic positioning elements

### 3. Game Mechanics

#### Movement System
- Grid-based movement (up, down, left, right)
- Stamina/energy management
- Collision detection
- Wrap-around grid boundaries

#### Treasure Collection
- Path finding to treasures
- Collection mechanics
- Value-based scoring system

#### Hunter Control
- Player-controlled hunter selection
- Skill-based advantages
- Status monitoring
- Rest and recovery mechanics

## Technical Implementation

### Dependencies
- Python 3.6+
- Core dependencies:
  - numpy
  - pandas
  - random2

### Development Tools
- Testing: pytest
- Code quality: flake8, black, mypy
- Coverage: pytest-cov

## Game Features

### 1. Interactive Gameplay
- Real-time grid visualization
- Command-based interaction
- Status monitoring
- Path finding assistance

### 2. Dynamic Configuration
- Customizable grid size
- Adjustable entity counts
- Balanced entity distribution
- Recommended configuration ranges

### 3. Visual Feedback
- Emoji-based grid representation
- Status indicators
- Movement feedback
- Collection notifications

## Testing
Comprehensive test suite covering:
- Treasure mechanics
- Simulation logic
- Knight behavior
- Hunter functionality
- Hideout operations

## Future Enhancements
1. Advanced AI for autonomous hunters
2. Multiplayer support
3. Extended treasure types
4. Enhanced visualization
5. Save/load game state
6. Achievement system

## Conclusion
Knights of Eldoria presents an engaging simulation environment that combines strategic gameplay with dynamic entity interactions. The modular architecture allows for easy extension and modification, while the comprehensive test suite ensures reliability and stability.

---

*Report generated based on project analysis* 

# File: /docs/readme.md
# Knights of Eldoria

This is a grid-based Python simulation featuring treasure hunters and knights navigating Eldoria in search of treasure.

## Setup
```bash
pip install -r requirements.txt
python src/main.py
```

## Features
- Hunters collect treasure and deposit it in hideouts
- Knights chase hunters and force them to drop their loot
- AI agents for movement logic

## Structure
- `/src`: Core logic
- `/tests`: Unit tests
- `/docs`: Report and diagrams


# File: /requirements.txt
numpy