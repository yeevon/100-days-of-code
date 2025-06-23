# Turtle Crossing Game 🐢🚗
## 📘 Overview
A simple arcade-style crossing game made with Python’s Turtle Graphics. The player controls a turtle trying to cross a road while dodging an endless stream of moving cars. Each successful crossing levels up the game and increases difficulty.

---------------
### 🧠 Features
- **Player Movement:**

  - Controlled with the Up arrow key

  - Moves vertically toward a finish line

- **Cars:**

  - Appear from the right and move left

  - Random colors and spawn intervals

  - Removed when off-screen

- **Collision Detection:**

  - Ends game if turtle collides with a car

- **Leveling System:**

  - Successful crossings increase the level

  - Car speed increases with each level

### 🗂️ Module Breakdown
**main.py**
- Initializes screen, game objects, and main loop

- Manages game progression, car spawning, and difficulty scaling

**player.py**
- Defines the Player class (the turtle)

- Handles movement, level detection, and reset

**car_manager.py**
- Defines the CarManager class

- Handles creation, movement, and cleanup of cars

**scoreboard.py**
- Displays and updates the current level

- Shows a “Game Over” message on collision

### 🎮 Controls
|**Action**	|**Key**|
|---------|--------|
|Move Up	|↑ Arrow|

### 💡 How the Game Scales
- Cars spawn more frequently and move faster as the level increases.

- Each level completion clears current cars before starting the next.