# Zillow Scraper & Google Forms Filler

This script scrapes Zillow listings using BeautifulSoup and submits the data to a Google Form using Selenium.

## Requirements
- Python
- Google Chrome & ChromeDriver
- `.env` file with:
  ```
  URL_ZILLOW=<Zillow_URL>
  URL_GOOGLE_FORMS=<Google_Forms_URL>
  ```

## Usage
1. Ensure ChromeDriver is installed.
2. Add Zillow and Google Forms URLs to `.env`.
3. Run the script:  
   ```
   python script.py
   ```

