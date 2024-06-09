from flask import Flask, request, render_template
from scraper import fetch_news  # Make sure it's using the updated version

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_digest():
    interests = request.form['interests']
    news_items = fetch_news(interests)
    return render_template('results.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True)
