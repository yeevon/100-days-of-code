# 🎉 Birthday Wisher - Extra Hard Project

This Python script automatically sends personalized birthday emails to friends or family based on data in a CSV file. It’s part of the **100 Days of Code** course – Day 32 (Extra Hard challenge).

---

## 💡 What I Learned

### ✅ Real-World Use of Python Libraries
- **pandas**: For working with tabular data in `birthdays.csv`, filtering by today's date, and updating the file.
- **smtplib**: For sending real emails using Gmail's SMTP server.
- **datetime**: To check if today's date matches any birthday.
- **random**: To select one of several letter templates at random.
- **os.environ**: For safely handling sensitive credentials via environment variables.

### ✅ Key Programming Concepts
- **Function modularization**: Each task (emailing, generating letters, updating the CSV) is separated into its own function for clarity and reusability.
- **File I/O**: Reading letter templates from `.txt` files and writing back to the CSV file when new people are added.
- **Conditional logic**: Skipping updates when `friend_family_list` is empty, and only sending emails if it's someone’s birthday.
- **Iterating over DataFrames**: Using `.iterrows()` to loop through matching birthday rows.
- **Avoiding common pitfalls**: Such as not calling `.iterrows()` correctly, or forgetting to use `.replace()` return values.

---

## 🛠 How It Works

1. **Load `birthdays.csv`**:
   A list of names, emails, and birthdates.

2. **Check today’s date**:
   Compare the current month and day with the CSV entries.

3. **If today is someone’s birthday**:
   - Pick a random letter from the `letter_templates` folder.
   - Replace `[NAME]` in the letter with the person’s actual name.
   - Send the email using Gmail.

4. **Optional**: Add new people to the list by editing `friend_family_list`.

---

## 📁 Project Structure
```yaml
project/
│
├── birthdays.csv
├── letter_templates/
│ ├── letter_1.txt
│ ├── letter_2.txt
│ └── letter_3.txt
├── main.py
└── README.md
```

---

## 🔒 Security Tip

Set your email password as an environment variable to avoid hardcoding:

```bash
export PW='your_email_app_password'
```
Then access it in Python via:
```python
os.environ['PW']
```

## ✅ Example CSV Format

```csv
name,email,year,month,day
Lucas de Lima,lucas@example.com,2015,12,5
Mimi de Lima,mimi@example.com,1982,7,18
```

