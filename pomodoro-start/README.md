# Pomodoro Stopwatch ⏱️🍅
## 📘 Overview
A Pomodoro-style timer app built with Tkinter that helps structure focused work sessions with alternating short and long breaks. This stopwatch visually guides users through work and break cycles and tracks progress using checkmarks.

---------

### 🧠 Features
- Pomodoro Cycles:

  - 25-minute work sessions

  - 5-minute short breaks

  - 15-minute long break after 4 work sessions

- Start/Reset Buttons: Begin or cancel the current timer cycle.

- Visual Timer: Displays countdown time and status ("Work" or "Break").

- Progress Tracking: Adds ✔ marks after each completed work session.
------------

### 🔁 How It Works
- start_counter() determines whether to start work or break based on repetition count (reps).

- count_down() manages time updates and triggers the next session on completion.

- reset_timer() cancels the timer and resets UI state and counters.

### 🖼️ UI Elements
|**Element**	|**Description**|
|----------|---------------|
|Canvas	|Shows a tomato image and timer text|
|Label	|Displays "Timer" / "Work" / "Break"|
|Buttons	|“Start” to begin, “Reset” to cancel|
|Checkmarks	|Tracks completed work sessions|

### 📂 Files
- main.py – Complete Pomodoro app logic and UI.

- tomato.png – Image used in the timer (must be in the same directory).