import requests
from datetime import datetime

MY_LAT = "29.693083"
MY_LNG = "-95.900337"
response = requests.get(url='http://api.open-notify.org/iss-now.json')

response.raise_for_status()

data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

print(iss_position)


parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

time_now = datetime.now()
print(data)
print(f"sunset: {sunset}, sunrise: {sunrise}, now: {time_now.hour}")