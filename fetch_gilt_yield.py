import requests
import beautifulsoup4
import pandas as pd
from datetime import datetime
import os



def scrape_investing_com():
    url = "https://www.investing.com/rates-bonds/uk-10-year-bond-yield"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        yield_value = soup.find("span", {"data-test": "instrument-price-last"}).text
        return yield_value
    except Exception as e:
        print(f"Scraping failed: {e}")
        return None

if __name__ == "__main__":
    scrape_investing_com()
