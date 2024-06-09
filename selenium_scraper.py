# selenium_scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_npr_news(interest=''):
    options = webdriver.ChromeOptions()
    options.headless = True  # Running headless to avoid UI pop-up during automation
    driver = webdriver.Chrome(options=options)

    # Go to NPR's news section
    driver.get("https://www.npr.org/sections/news/")

    try:
        # Click "Load more stories" button multiple times
        for _ in range(5):  # Load more articles
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.options__load-more'))
            )
            load_more_button.click()
            time.sleep(2)  # Wait for the content to load

        # Now scrape the articles
        articles = WebDriverWait(driver, 10).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, 'article'))
        news_items = []
        for article in articles:
            title = article.find_element(By.CSS_SELECTOR, 'h2').text
            summary = article.find_element(By.CSS_SELECTOR, 'p').text
            if interest.lower() in title.lower() or interest.lower() in summary.lower():
                news_items.append({'title': title, 'summary': summary})
        return news_items
    finally:
        driver.quit()

if __name__ == "__main__":
    scraped_data = scrape_npr_news("climate change")  # Example interest
    print(scraped_data)  # Output the data
