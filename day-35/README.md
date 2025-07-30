# ☔ Weather Alert SMS Bot
A simple Python script that checks the upcoming weather forecast using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is likely.

--------------------
## Features
- Checks weather forecast for a specific location.
- Sends an SMS if precipitation is expected.
- Uses environment variables to securely manage credentials.
- Runs with minimal dependencies.

-----------
## How It Works
1. Calls the OpenWeatherMap 5-day forecast API using latitude/longitude.
2. Parses the weather codes from the forecast.
3. If any weather code indicates rain (code < 700), it sends a sweet SMS warning using Twilio.

----------
##️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-sms-bot.git
cd weather-sms-bot
```
### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
Create a .env file in the root directory:

```dotenv
API_KEY=your_openweathermap_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
MY_NUMBER=+1234567890       # Twilio phone number
MIMI_NUMBER=+1098765432     # Destination phone number
```
⚠️ Never commit your .env file to version control! Add it to your .gitignore.

-------
## Example Output
If rain is detected in the forecast:

```csharp
Hey babe if your going out, bring an umbrella!
```

## 🧪 Running the Script
```bash
python main.py
```
Or schedule it with a cron job for regular checks.

-------------

## 📚 Weather Code Reference
Weather codes below 700 indicate various forms of precipitation (rain, snow, drizzle, etc.), based on https://openweathermap.org/weather-conditions
