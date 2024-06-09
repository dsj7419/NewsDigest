from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import requests
from bs4 import BeautifulSoup

def scrape_npr_news(interest=''):
    service = Service(executable_path='G:\\Projects\\Gekodriver\\geckodriver.exe')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://www.npr.org/sections/news/")

    def close_popups():
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "article.pn-modal"))
            )
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "article.pn-modal button.pn-modal__close"))
            )
            close_button.click()
            print("Overlay dismissed.")
        except (TimeoutException, NoSuchElementException) as e:
            print("No overlay found or clickable element:", str(e))

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        for _ in range(5):  # Adjust the range as necessary
            close_popups()
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.options__load-more'))
            )
            load_more_button.click()
            time.sleep(2)  # Allow time for any potential overlays to appear
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down
            time.sleep(2)  # Allow more time for dynamic content
            close_popups()

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        articles = soup.find_all('article', class_='item has-image')
        news_list = []

        for article in articles:
            title = article.find('h2', class_='title').text.strip() if article.find('h2', class_='title') else 'No Title Available'
            summary = article.find('p', class_='teaser').text.strip() if article.find('p', class_='teaser') else 'No Summary Available'
            if interest.lower() in title.lower() or interest.lower() in summary.lower():
                category = article.find('h3', class_='slug').text.strip() if article.find('h3', class_='slug') else 'No Category Available'
                link = article.find('h2', class_='title').find('a')['href'] if article.find('h2', class_='title') else 'No Link Available'
                date = article.find('time').text.strip() if article.find('time') else 'No Date Available'
                image_url = article.find('img')['src'] if article.find('img') else 'default-image-url.jpg'
                news_list.append({
                    'title': title,
                    'summary': summary,
                    'category': category,
                    'link': link,
                    'date': date,
                    'image': image_url
                })

        return news_list
    finally:
        driver.quit()

if __name__ == "__main__":
    scraped_data = scrape_npr_news("climate change")
    print(scraped_data)
