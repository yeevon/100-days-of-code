# NATO Phonetic Alphabet Converter 🔡➡️📻
## 📘 Overview
This script converts any word entered by the user into its NATO phonetic alphabet equivalent using data from a CSV file. It demonstrates data loading with pandas, dictionary comprehensions, and basic error handling with recursion.

---------------

### 🧠 Features
- Loads the NATO alphabet data from nato_phonetic_alphabet.csv.

- Creates a dictionary mapping each letter to its phonetic code.

- Takes user input, converts it to uppercase, and prints the corresponding list of phonetic words.

- Handles invalid input (e.g., numbers or symbols) with an error message and retries input.

--------------

### 🧪 Example
**Input:**
```
Enter a word: chat
```
**Output:**
```
['Charlie', 'Hotel', 'Alpha', 'Tango']
```
---------------

### 📂 Files
- main.py – Main script.

- nato_phonetic_alphabet.csv – CSV file containing letter-to-code mappings.