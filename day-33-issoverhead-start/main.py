import os
from time import sleep
from dotenv import load_dotenv
import requests
import smtplib
from datetime import datetime

load_dotenv()
MY_LAT = 29.693083 # Your latitude
MY_LONG = -95.900337 # Your longitude


# Send Email ISS is Overhead
def send_email():
    email = "delimajm@gmail.com"
    password = os.environ['PW']

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="mimi_m20@hotmail.com",
            msg=f"Subject:Look Up\n\nQuick go outside you can see the ISS fly by!!"
        )

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return (True if (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
                     and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5)
            else False)

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunset = sunset if sunset > 4 else 24 + sunset  - 5
    time_now = datetime.now().hour

    return True if time_now >= sunset and (time_now > 12 or time_now <= sunrise) else False

while True:
    sleep(60)
    if is_dark() and is_iss_overhead(): send_email()



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



