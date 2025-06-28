# Day 30 – Working with try, except, else, and finally
## 📘 Overview
Practiced handling exceptions in Python using structured error handling with try, except, else, and finally blocks. This allows for safe file operations and error recovery in potentially risky code.

------------------

### 🧠 Concepts Demonstrated
- try block:

  - Attempts to open and read from a file (a_file.txt).

  - Tries to access a dictionary key.

- except FileNotFoundError:

  - Catches the case where the file does not exist.

  - Creates the file and writes default content ("Something").

- else block:

  - Executes if no exception was raised.

  - Reads and prints the file content.

- finally block:

  - Ensures that the file is closed regardless of whether an error occurred.