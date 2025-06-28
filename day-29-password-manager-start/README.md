# Password Manager 🔐
## 📘 Overview
A full-featured password manager built with Tkinter for the GUI, capable of generating secure passwords, saving credentials, and searching for stored entries. Data is stored in a local JSON file.

------

### 🧠 Features
#### ✅ Password Generation
- Randomly generates strong passwords with:

  - Letters (uppercase and lowercase)

  - Numbers

  - Symbols

- Automatically copies the password to the clipboard.

#### ✅ Save Credentials
- Saves website, email/username, and password.

- Data is structured and stored in a data.json file using nested dictionaries.

- Prevents saving if required fields are left empty.

#### ✅ Search Functionality
- Retrieves saved credentials based on the website name.

- Displays stored email and password in a popup window.

- Gracefully handles missing files or unknown entries.

### 🖼️ UI Layout
Widget	Description
Entry Fields	Website, Email/Username, Password
Buttons	Search, Generate Password, Add
Canvas	Displays logo image
Labels	Guide user input

### 📂 Files
main.py – Main application logic and GUI.

data.json – Automatically created/stored credentials file.

logo.png – Image file for the application header (must exist for UI to render properly).