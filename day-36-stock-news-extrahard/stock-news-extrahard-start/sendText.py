import os
from twilio.rest import Client

class SendText():

    def __init__(self, 
                 up_down: bool,
                 percent_change: float,
                 articles: list,
                 stock: str
                 ):
        
        self.arrow = "🔺" if up_down else "🔻"
        self.text = f"{stock}: {self.arrow}{percent_change}\n"
        self.articles = articles
        self.percent_change = percent_change
        self._generate_message()
        
    def _generate_message(self):
        
        for article in self.articles:
            self.text += f"Headline: {article['title']}\n"
            self.text += f"Brief: {article['description']}"

            if article != self.articles[-1]:
                self.text += "\n\n"

    def send_message(self):
        account_sid = os.environ["TWILIO_SID"]
        auth_token = os.environ["TWILIO_TOKEN"]
        client = Client(account_sid, auth_token)

        if len(self.text) > 200:
            newtext = self.text[:150]
        else:
            newtext = self.text

        message = client.messages.create(
            body=f"Stock updates, {newtext}",
            from_=os.environ["TWILIO_NUMBER"],
            to=os.environ["MY_NUMBER"],
        )

        print(message.status)