# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A classic Snake game implementation in Python. This is a new project being initialized.

## Development Setup

**Python Version**: Python 3.8+ recommended

**Dependencies**:
- `pygame` for game rendering and input handling
- Standard library modules for game logic

**Installation**:
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Running the Game**:
```bash
python main.py
# or
python snake_game.py
```

## Architecture

### Core Components

**Game Loop Structure**:
- Main game loop handling events, updates, and rendering at 60 FPS
- Input handling for arrow keys/WASD controls
- Collision detection for walls, self-collision, and food
- Score tracking and display

**Game State Management**:
- Snake representation as list of coordinate segments
- Direction state with prevention of 180-degree turns
- Food position generation with collision avoidance
- Game over detection and restart capability

**Rendering System**:
- Grid-based coordinate system (typically 20x20 or 30x30)
- Snake segments rendered as rectangles
- Food rendered distinctly from snake
- Score display and game over screen

### File Organization

Expected structure:
- `main.py` or `snake_game.py`: Entry point and main game loop
- `snake.py`: Snake class with movement and collision logic
- `food.py`: Food generation and positioning
- `game.py`: Game state management and coordination
- `constants.py`: Configuration (grid size, colors, speed)
- `utils.py`: Helper functions (drawing, collision detection)

## Game Mechanics

**Movement**:
- Snake moves continuously in current direction
- New head position calculated based on direction
- Tail removed unless food is eaten
- Movement speed controlled by FPS and update frequency

**Collision Detection**:
- Wall collision: Check if head position exceeds grid boundaries
- Self-collision: Check if head position matches any body segment
- Food collision: Check if head position matches food position

**Growth**:
- When food is eaten, tail segment is not removed
- New food spawns at random unoccupied position
- Score increments

## Development Guidelines

**Code Organization**:
- Separate game logic from rendering
- Use classes for Snake, Food, and Game entities
- Keep constants in dedicated file for easy tuning
- Implement clean separation between input, update, and render phases

**Performance Considerations**:
- Use pygame's clock for consistent FPS
- Optimize collision detection for larger grids
- Minimize object creation in game loop

**Testing Approach**:
- Manual testing for gameplay feel
- Unit tests for collision detection logic
- Test edge cases (spawning food when grid is nearly full)
- Verify no 180-degree turn exploitation

## Common Development Tasks

**Adjusting Difficulty**:
- Modify FPS/speed in constants
- Adjust grid size for more/less space
- Implement progressive speed increases

**Adding Features**:
- High score persistence (JSON file or SQLite)
- Multiple difficulty levels
- Obstacles/walls within grid
- Different game modes (timed, survival)
- Sound effects and background music

**Debugging**:
- Print snake position and length for movement issues
- Visualize collision boxes for debugging detection
- Log food spawn positions to verify randomization
