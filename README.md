# News Digest

## Introduction
The News Digest application is designed to scrape news articles from NPR's news section. This project serves as a proof of concept for web scraping techniques, particularly focusing on dynamic content handling and popup interactions. While the tool specifically targets the NPR website, the methods and patterns used can be adapted for scraping various other news sources.

This application was created as a test project to explore and demonstrate the capabilities of web scraping in situations where an API is not available or lacks certain functionalities. It's important to note that using APIs is generally preferred for data extraction due to reliability, speed, and compliance with terms of service. This project should therefore be used for educational purposes and personal projects that comply with NPR's scraping policies.

## Prerequisites
To run the News Digest application, you will need:

- Python 3.8 or higher
- pip (Python package installer)

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/news-digest.git
   cd news-digest
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python News_Digest.py
   ```

## Usage
To use the application, simply run the script and input your interests when prompted. The script will automatically handle pop-ups and extract relevant news articles based on your input.

## Note
This scraper is only intended for educational use and personal projects. Always ensure compliance with NPR's terms of service and avoid excessive requests that might impact the NPR servers.

