import requests, os
from datetime import datetime, timedelta
from getArticles import GetArticles
from sendText import SendText

class AnalyzeStock():

    def __init__(self, stock: str, company: str):
        
        self.up_down = None
        self.stock = stock
        self.company = company

        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock,
            "apikey": os.environ.get("API_KEY")
        }

        response = requests.get("https://www.alphavantage.co/query", params=params)
        response.raise_for_status()
        self.data = response.json()

    def _get_percent_change(self) -> float:
        time_series_data = self.data["Time Series (Daily)"]

        dt = datetime.now().date() - timedelta(days=1)

        if dt.weekday() > 4:
            dt = dt - timedelta(days=(dt.weekday()-4))

        last_close_price = float(time_series_data[str(dt)]["4. close"])
        

        # get previous dates closing price
        prev_dt = dt - timedelta(days=(1))

        if prev_dt.weekday() > 4:
            prev_dt = prev_dt - timedelta(days=(prev_dt.weekday()-4))

        previous_close_price = float(time_series_data[str(prev_dt)]["4. close"])

        self.up_down = last_close_price > previous_close_price

        return (1 - (previous_close_price / last_close_price))
    

    def update_user(self):
        pc = self._get_percent_change()

        if pc > 0.05:
            ga = GetArticles(self.company)
            print(f"articles: {ga.articles_to_text}")
            if ga.articles_to_text:
                st = SendText(
                    up_down=self.up_down, 
                    stock=self.stock,
                    articles=ga.articles_to_text,
                    percent_change=pc
                    )
                
                st.send_message()