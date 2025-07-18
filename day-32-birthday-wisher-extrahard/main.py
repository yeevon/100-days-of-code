##################### Extra Hard Starting Project ######################
import os

import pandas as pd
import datetime as dt
import smtplib
import random

# Optional: list of new people to add
# Values should match df_column structure
friend_family_list = []
df_columns = ['name', 'email', 'year', 'month', 'day']
df = pd.read_csv("birthdays.csv")


# Send birthday email
def send_email(letter: list, bd_email):
    email = "delimajm@gmail.com"
    password = os.environ['PW']

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=bd_email,
            msg=f"Subject:Best Wishes\n\n{"".join(letter)}"
        )

# Generate birthday letter
def generate_letter(gen_row) -> list:
    random_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_num}.txt") as bDay_letter:
        letter_content = [item for item in bDay_letter]
        letter_content[0] = letter_content[0].replace("[NAME]", gen_row["name"])

    return letter_content

# update csv with new family members
def update_csv(update_df):
    for person in friend_family_list:
        if person[0] not in update_df["name"].values:
            add_person = pd.DataFrame([dict(zip(df_columns, person))])
            update_df = pd.concat([update_df, add_person], ignore_index=True)

    df.to_csv("birthdays.csv", index=False)


if friend_family_list: update_csv(df)

# Check if its someone's birthdate
today = dt.datetime.now()
birth_day = df[(df["month"] == today.month) & (df["day"] == today.day)]

if not birth_day.empty:
    for index, row in birth_day.iterrows():
        send_email(generate_letter(row), row['email'])

