import requests
from bs4 import BeautifulSoup

class CryptocurrencyNewsAggregator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.articles = []

    def fetch_news_articles(self, source):
        # Fetch news articles from the specified source using the API or web scraping
        if source == "api":
            self.fetch_news_articles_from_api()
        elif source == "website":
            self.fetch_news_articles_from_website()
        else:
            print("Invalid news source.")

    def fetch_news_articles_from_api(self):
        # Fetch news articles from the news API using the provided API key:
        url = f"https://api.example.com/news?api_key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            self.articles = response.json()
        else:
            print("Error fetching news articles from the API.")

    def fetch_news_articles_from_website(self):
        # Fetch news articles from the website using web scraping
        url = "https://www.example.com/news"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract relevant data from the webpage using BeautifulSoup
            # and add it to self.articles list
            # Example: self.articles = soup.find_all('div', class_='article')
        else:
            print("Error fetching news articles from the website.")

    def filter_articles_by_keyword(self, keyword):
        # Filter articles based on a specified keyword
        filtered_articles = []

        for article in self.articles:
            if keyword.lower() in article['title'].lower() or keyword.lower() in article['content'].lower():
                filtered_articles.append(article)

        self.articles = filtered_articles

    def present_articles(self):
        # Present the aggregated news articles in a readable format
        for article in self.articles:
            print("Title:", article['title'])
            print("Source:", article['source'])
            print("Published At:", article['published_at'])
            print("Content:", article['content'])
            print("-----------------")

# Example usage:

# Define API key
api_key = "your_api_key"

# Create an instance of CryptocurrencyNewsAggregator
news_aggregator = CryptocurrencyNewsAggregator(api_key)

# Fetch news articles from the desired source (API or website)
news_aggregator.fetch_news_articles("api")

# Filter articles based on a keyword (optional)
keyword = "bitcoin"
news_aggregator.filter_articles_by_keyword(keyword)

# Present the aggregated news articles
news_aggregator.present_articles()
