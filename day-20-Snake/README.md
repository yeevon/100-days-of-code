# Snake Game 🐍 (Turtle Graphics)
## 📘 Overview
A classic Snake game built using Python’s Turtle graphics module. The player controls a growing snake to eat randomly placed food while avoiding wall collisions and self-collision. The game keeps track of both current and high scores.

---------------
### 🧠 Features
- Real-Time Movement: Arrow key controls for smooth directional input.

- Food Mechanics: Randomly spawning food that increases score and snake length.

  - Collision Detection:

  - Ends game when the snake hits the wall or itself.

- Resets snake position and score but preserves high score.

Persistent High Score: Stored in data.txt.
--------------
### 🗂️ Module Breakdown
#### main.py
- Initializes the screen and game objects.

- Handles game loop, event listening, and collision checks.

#### snake.py
- Defines the Snake class and manages:

  - Movement logic

  - Growth

  - Reset after collision

#### food.py
- Defines the Food class.

- Spawns food in random locations using refresh() method.

#### scoreboard.py
- Displays and updates the score.

- Reads and writes high score from/to data.txt.
------------------
### 🎮 Controls
|**Action**	|**Key**|
|---------|--------|
|Move Up	|↑ Arrow|
|Move Down	|↓ Arrow|
|Move Left	|← Arrow|
|Move Right	|→ Arrow|
-----------------------
### 📂 Required Files
- data.txt – A simple file to store the high score (must exist or be auto-generated).

- All .py files: main.py, snake.py, food.py, scoreboard.py