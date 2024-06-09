# News_Digest.py
from flask import Flask, render_template, request
from selenium_scraper import scrape_npr_news  # Import the Selenium scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_digest():
    interest = request.form['interests']
    news_items = scrape_npr_news(interest)  # Pass the interest to the Selenium scraper
    return render_template('results.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True)
