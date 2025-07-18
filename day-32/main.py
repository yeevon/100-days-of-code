# import smtplib
#
# my_email = "delimajm@gmail.com"
# password = "fgfcekbgfgicfewl"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="mimi_m20@hotmail.com",
#         msg="Subject:Hello\n\nTesting SMTP"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
#
# year = now.year
# print(year)
# print(type(year))
#
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year=1983, month=8, day=7)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

FRIDAY = 4
now = dt.datetime.now()
my_email = "delimajm@gmail.com"
password = "fgfcekbgfgicfewl"

if now.weekday() == FRIDAY:
    with open("quotes.txt") as quotes:
        quotes_list = [quote for quote in quotes]

    quote_of_the_day = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mimi_m20@hotmail.com",
            msg=f"Subject:Motivation from your Hubby\n\n{quote_of_the_day}\n\n "
                f"Love your hubby"
        )