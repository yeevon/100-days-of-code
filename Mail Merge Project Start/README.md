# Mail Merge – Personalized Letter Generator
## 📘 Overview
This project automates the process of generating personalized invitation letters by merging names from a list into a templated letter. The output is saved as individual text files, ready to send.

-----------

### 🧠 Features
- Reads a list of names from invited_names.txt.

- Loads a letter template from starting_letter.txt.

- Replaces the placeholder [name] in the template with each actual name.

- Saves the personalized letters to the Output/ReadyToSend/ directory.
----------

### 📂 File Structure
```css
Input/
├── Names/
│   └── invited_names.txt
├── Letters/
│   └── starting_letter.txt

Output/
└── ReadyToSend/
    └── [Generated letters]
```
-----------

### 🧪 How It Works
1. Each name from invited_names.txt is stripped of newline characters.

2. [name] in the template is replaced with the actual name.

3. A new file is written for each invite in the ReadyToSend folder.