import requests

# Constants
API_KEY = 'f14de68c0d534011a8f927dd7b9ec898'
BASE_URL = 'https://newsapi.org/v2/everything'

def fetch_news(query, language='en'):
    """Fetch news articles from the News API based on the query."""
    params = {
        'q': query,
        'apiKey': API_KEY,
        'language': language
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data.get('articles', [])

def parse_articles(articles):
    """Extract relevant information from news articles."""
    parsed_articles = []
    for article in articles:
        parsed_articles.append({
            'title': article.get('title'),
            'link': article.get('url'),
            'description': article.get('description'),
            'publishedAt': article.get('publishedAt')
        })
    return parsed_articles

def filter_articles(articles, keywords):
    """Filter articles based on user-provided keywords."""
    filtered_articles = [
        article for article in articles
        if any(keyword.lower() in article['title'].lower() for keyword in keywords)
    ]
    return filtered_articles

def display_articles(articles):
    """Display the list of articles to the user."""
    if not articles:
        print("No articles found.")
        return
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Description: {article['description']}")
        print(f"Published At: {article['publishedAt']}")
        print('-' * 80)

def main():
    """Main function to run the news aggregator."""
    query = input("Enter search query: ")
    keywords = input("Enter keywords (comma-separated): ").split(',')

    articles = fetch_news(query)
    parsed_articles = parse_articles(articles)
    filtered_articles = filter_articles(parsed_articles, keywords)

    print(f"\nNews Articles for '{query}':")
    display_articles(filtered_articles)

if __name__ == '__main__':
    main()