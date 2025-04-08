import requests
import beautifulsoup
import pandas as pd
from datetime import datetime
import os

def get_10y_gilt_yield():
    url = "https://www.bankofengland.co.uk/boeapps/database/fromshowcolumns.asp"
    params = {
        "Travel": "NIxSTx",
        "SeriesCodes": "IUDSNPY",  # Verify this code is correct
        "Datefrom": datetime.today().strftime('%d/%m/%Y'),
        "Dateto": datetime.today().strftime('%d/%m/%Y'),
        "CSVF": "TT",
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = pd.read_csv(pd.compat.StringIO(response.text))
        latest_yield = data.iloc[-1]["IUDSNPY"]
        print(f"10-year UK gilt yield: {latest_yield}%")
        
        # Write to file for GitHub Actions
        with open('yield.txt', 'w') as f:
            f.write(str(latest_yield))
    else:
        raise Exception("Failed to fetch data")



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
    get_10y_gilt_yield()
