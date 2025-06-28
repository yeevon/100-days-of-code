# Quiz Game ❓🧠
## 📘 Overview
A command-line trivia quiz game built in Python using the Open Trivia Database API. The user answers True/False questions and receives immediate feedback and scoring.

---
## 🧠 Features
- Fetches real-time trivia questions via API

- Supports game customization:

  - Number of questions

  - Category selection

  - Difficulty level (Easy, Medium, Hard)

- Provides instant correctness feedback

- Tracks and displays score after each question
---
## 🎮 How to Play
1. Run the game:
    ```bash
    python app.py
    ```
2. Choose whether to customize the game.

3. Answer each question with True or False.
---
## 🗂️ Modules
```app.py```
- Handles user interaction and game loop

- Prompts for input, calls Questions class

```questions.py```
- Fetches trivia data from the API

- Manages question list, scoring, and answer validation

- Categories supported:

  - General Knowledge

  - Books

  - Film

  - Music

  - Musicals

  - Television

  - Video Games

## 🧪 Sample Run
```
Welcome to the Quiz Game!
Do you want to customize the game? (Yes/No): no
Q.1: The Great Wall of China is visible from the Moon. (True/False)?: False
You got it right!
The correct answer was: False.
Your current score is: 1/1
```