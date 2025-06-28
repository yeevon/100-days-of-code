# Turtle Race Game 🐢🏁
## 📘 Overview
A simple and fun turtle racing game built using Python’s Turtle Graphics. Players bet on which turtle (by color) will win a randomly driven race across the screen.

---
## 🧠 Features
- Six turtles of different colors race across the screen

- User places a bet on a color before the race begins

- Turtles move forward by random distances on each frame

Game announces win/loss based on the player's bet
---
## 🎮 How to Play
1. Run the game:

    ```bash
    python main.py
    ```
2. Enter a color when prompted (e.g., red, blue, etc.)

3. Watch the race and see if your turtle wins!
---
## 🐢 Turtle Colors
red

orange

green

blue

purple

black
---
## 📐 Technical Notes
Uses turtle module for drawing and movement

random.randint(0, 10) controls turtle step size

Checks .xcor() to determine when a turtle finishes the race