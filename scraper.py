import requests
from bs4 import BeautifulSoup

def fetch_news(interest=''):  # Accept an interest parameter
    url = 'https://www.npr.org/sections/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='item has-image')
    news_list = []
    for article in articles:
        title = article.find('h2', class_='title').text.strip() if article.find('h2', class_='title') else 'No Title Available'
        summary = article.find('p', class_='teaser').text.strip() if article.find('p', class_='teaser') else 'No Summary Available'
        
        # Filter the articles to only include those that contain the interest keyword in the title or summary
        if interest.lower() in title.lower() or interest.lower() in summary.lower():
            category = article.find('h3', class_='slug').text.strip() if article.find('h3', class_='slug') else 'No Category Available'
            link = article.find('h2', class_='title').find('a')['href'] if article.find('h2', class_='title') else 'No Link Available'
            date = article.find('time').text.strip() if article.find('time') else 'No Date Available'
            
            news_list.append({
                'title': title,
                'summary': summary,
                'category': category,
                'link': link,
                'date': date
            })
    return news_list
