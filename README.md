# Cryptocurrency News Aggregator

That project collects and displays news articles and updates from various cryptocurrency-related sources:

 - This script is implemented the following features...

__1. Data Retrieval:__

 - The ```fetch_news_articles``` method fetches news articles from the specified source (API or website) using the ```fetch_news_articles_from_api``` or ```fetch_news_articles_from_website``` methods.
   
__2. Data Filtering:__

 - The ```filter_articles_by_keyword``` method filters articles based on a specified keyword. Articles that contain the keyword in their title or content are retained, and the filtered articles are stored in the ```self.articles``` list.

__3. Presentation:__

 - The ```present_articles``` method presents the aggregated news articles in a readable format by iterating through each article and printing its title, source, published date, and content.

__Code Usage:__

- Following libraries are required to be installed before running the code.
  ```bash
  pip install requests
  pip install beautifulsoup4
  ```
- To use this code, replace the ```api_key``` variable with your actual API key if you choose to fetch news articles from an API. Additionally, customize the web scraping logic in the ```fetch_news_articles_from_website``` method to extract relevant data from the website you want to scrape.


   
