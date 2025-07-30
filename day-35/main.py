from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

LATITUDE = 19.075983
LONGITUDE = 72.877655
RESULT_COUNT = 4
api_key = os.environ.get("API_KEY")


def send_sms(text):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Hey babe if your going out, {text}",
        from_=os.environ["MY_NUMBER"],
        to=os.environ["MIMI_NUMBER"],
    )

    print(message.Status)


params = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'cnt': RESULT_COUNT,
    'appid': api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

data = response.json()

# Gets the weather id from the first weather item returned in the list of forcast from openweathermap api
weather_code = [code['weather'][0]['id'] for code in data['list']]

if any(x < 700 for x in weather_code):
    send_sms("bring an umbrella!")


