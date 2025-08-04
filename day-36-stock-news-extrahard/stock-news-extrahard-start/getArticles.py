import os, requests
from datetime import datetime, timedelta

class GetArticles():

    def __init__(self, company_name: str):

        dt = datetime.now().date()

        params = {
            "q": company_name,
            "from": str(dt - timedelta(days=7)),
            "to": str(dt),
            "sortBy": "popularity",
            "pageSize": 3,
            "apiKey": os.environ.get("API_KEY_2")
            }

        response = requests.get("https://newsapi.org/v2/everything", params=params)
        response.raise_for_status()
        
        self.news_data = response.json()
        self.articles_to_text = []
        self._generate_article()

    def _generate_article(self):

        with open("news_articles.txt", 'w+') as na:
            for article in self.news_data["articles"]:

                news_title = article["title"]
                news_description = article["description"]

                na.write(f"Title: {news_title}\n\n") 
                na.write(f"Published: {article["publishedAt"].split('T')[0]}, ") 
                na.write(f"Publisher: {article["source"]["name"]}\n\n")
                
                author = article["author"] or "Unknown Author"

                if '\n' in author:
                    author = author.split('\n')[0]

                na.write(f"{author}\n\n")

                na.write(f"{article["content"]}\n")
                na.write(f"Link to full article: {article["url"]}\n")
                na.write("-"*200)
                na.write("\n\n\n")

                self.articles_to_text.append({'title': news_title, 'description': news_description})