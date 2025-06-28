# 📘 Flashy – French Flashcard App
A simple, interactive flashcard app built with Python and Tkinter to help you learn French vocabulary through spaced repetition.

## Features
- Random French words shown as flashcards

- Auto-flip to English translation after 3 seconds

- Save known words by clicking the checkmark — they won’t appear again

- Skip words with the X button to review them again later

- Progress is saved between sessions (words_to_learn.csv)

## 🗂️ File Structure
```bash
project/
│
├── main.py                 # Main application logic
├── data/
│   ├── french_words.csv    # Full vocabulary list (used on first launch)
│   └── words_to_learn.csv  # Automatically generated as you learn
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
```
## 📦 Requirements
- Python 3.x

- pandas

- tkinter (standard with most Python installations)

Install pandas if needed:
```bash
pip install pandas
```

##  🛠️ How It Works
1. On launch, it loads words_to_learn.csv if it exists, else defaults to french_words.csv.

2. A French word is displayed.

3. After 3 seconds, it flips to show the English translation.

4. Click:

    - ✅ Right to mark the word as known (it gets removed from the list).

    - ❌ Wrong to skip and see it again later.

5. Progress is saved automatically to words_to_learn.csv.

## 🧪 Running the App
Just run:
```bash
python main.py
```
Make sure you're in the directory containing main.py and that the data/ and images/ folders are set up correctly.

## 📎 Notes
- You can reset your progress by deleting data/words_to_learn.csv.

- Make sure all image file paths are correct; otherwise, Tkinter will raise errors.