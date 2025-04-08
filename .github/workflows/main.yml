import requests
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

if __name__ == "__main__":
    get_10y_gilt_yield()
