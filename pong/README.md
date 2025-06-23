# Pong Game 🎮 (Turtle Graphics)
## 📘 Overview
A recreation of the classic Pong game using Python’s Turtle Graphics module. Two players control paddles to bounce the ball back and forth. Points are scored when the opponent misses the ball.

----------------

### 🧠 Features
- Two-player paddle control (W/S for left, Up/Down for right)

- Ball bounces off walls and paddles

- Scoreboard tracks and displays each player's score

- Ball resets on missed catch and increases speed with each hit

### 🗂️ Module Breakdown
#### main.py
- Sets up screen and game loop

- Handles keyboard input

- Manages collision detection and score tracking

#### paddle.py
- Defines Paddle class with movement logic

- Includes methods to move paddle up/down

#### ball.py
- Controls ball behavior: movement, bouncing, collision detection

- Resets ball position on score

- Increases speed after paddle collision

#### score.py
- Displays and updates score for both players

- Writes score using Turtle graphics

### 🎮 Controls
|**Player**	|**Move Up**	|**Move Down**|
|----------|------------|------------|
|Left Paddle|	W	|S|
|Right Paddle|	↑	|↓|

### 📐 Screen Layout
- Window Size: 800x600 pixels

- Ball starts in center and moves diagonally

- Paddles placed near the left and right edges

- Score displayed at top center