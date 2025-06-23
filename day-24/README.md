# Day 24 – Reading and Writing Text Files in Python
## 🌱 What I Learned
Today, I practiced how to read from and write to .txt files using Python’s built-in open() function. This is a foundational skill for handling file I/O in many real-world applications such as logs, config files, and basic data storage.

### 🧠 Key Concepts
- Reading a file: Using open() with default 'r' mode to access file contents.

- Writing to a file: Using open() with 'w' mode to overwrite or create new files.

- File operations are automatically closed when using the with context manager.

### 🧪 Example Code
```python
# Reading from a file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing to a new file (or overwriting if it exists)
with open("new_file.txt", mode="w") as file:
    file.write("\nnew text.")
 ```
### 📁 Files Created
- my_file.txt – Used for reading content.

- new_file.txt – Created/written with new text content.