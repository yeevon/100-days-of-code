# 📈 Day 36 – Stock News Extra Hard

This Python script checks the daily stock price of a selected company and fetches recent news articles if there's a significant price change. It also sends SMS alerts via Twilio with the latest headline summaries.

## 🔧 Project Overview

This challenge combines data from the following APIs:

- **Alpha Vantage** for stock data
- **NewsAPI** for recent news headlines
- **Twilio API** for sending SMS alerts

---

## 📂 Project Structure

```init
Day36-stock-news-extrahard/
├── main.py # Orchestrates logic: stock check → news → SMS
├── analyzeStock.py # Checks price difference and pulls news if needed
├── sendText.py # Sends SMS alerts via Twilio
├── .env # Stores API keys and sensitive config
├── README.md # This file
├── requirements.txt # Project dependencies
```

---

## 🛠️ Features

- Detects stock price changes between yesterday and the day before
- Sends news articles only if the price change exceeds a 5% threshold
- Parses and sends top 3 related news headlines via SMS

---

## 🔑 Environment Variables (`.env`)

You must create a `.env` file in the root directory with the following:

```env
STOCK=TSLA
COMPANY_NAME=Tesla Inc
API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
MY_NUMBER=+1234567890         # Your Twilio number
MIMI_NUMBER=+1987654321       # Destination number
```

---

### ▶️ How to Run

Install dependencies:

```bash
    pip install -r requirements.txt
```

Run the project:

```bash
    python main.py
```

---

## Dependencies

```nginx
requests
python-dotenv
twilio
```

Install with:

```bash
pip install requests python-dotenv twilio
```

## Sample Output

SMS Message (if triggered):

```init
📉 TSLA: -5.7%
Tesla stock drops after earnings report.
https://news.example.com/tesla-earnings
```

---

## Limitations

- Free API tiers have rate limits (5/min for Alpha Vantage, 100/day for NewsAPI)

- Twilio free accounts prepend branding in SMS

## Concepts Practiced

- API requests and parameter formatting
- Working with dates and JSON data
- Modular Python scripting
- Environment variable management with dotenv
- Integrating third-party services (Twilio)

---
