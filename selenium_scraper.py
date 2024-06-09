from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import time

def scrape_npr_news(interest=''):
    service = Service(executable_path='G:\\Projects\\Gekodriver\\geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://www.npr.org/sections/news/")

    try:
        # Wait for the entire page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        # Attempt to close any pop-ups or overlays
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".tp-modal .tp-close, .tp-backdrop, .tp-modal"))
            ).click()
            print("Modal or overlay dismissed")
        except TimeoutException:
            print("No modal or overlay to dismiss")

        # Click "Load more stories" button multiple times
        for _ in range(5):
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.options__load-more'))
            )
            load_more_button.click()
            time.sleep(2)  # Allow time for the page to load more content

        # Scrape the articles
        articles = driver.find_elements(By.CSS_SELECTOR, 'article')
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
    scraped_data = scrape_npr_news("climate change")
    print(scraped_data)
