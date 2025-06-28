# Day 17 – Interactive Turtle Controller 🐢🎮
## 📘 Overview
Built an interactive turtle control system using the Turtle graphics module. This script responds to real-time keyboard input for smooth directional movement — both linear and rotational.

---
## 🧠 Features
- Continuous turning:

  - Hold W for clockwise rotation

  - Hold S for counterclockwise rotation

- Linear movement:

  - Press D to move forward

  - Press A to move backward

- Clear screen:

  - Press C to reset the turtle to the center

- Uses onkeypress, onkeyrelease, and ontimer for real-time input and animation
---
## 🎮 Controls
|**Key**	|**Action**|
|-----------|-----------|
|W	|Rotate clockwise (hold)|
|S	|Rotate counterclockwise (hold)|
|D	|Move forward (press)|
|A	|Move backward (press)|
|C	|Clear screen and reset|
---
## 🧪 Technical Highlights
- Uses ontimer() for smooth rotation over time

- Demonstrates use of global flags for continuous movement

- Combines both event-based and loop-based animation