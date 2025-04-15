# boe_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get('https://www.bankofengland.co.uk')
    time.sleep(3)

    rate_box = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.bank-rate'))
    )

    current_rate = WebDriverWait(rate_box, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.bank-rate__rate'))
    ).text.strip()

    decision_date = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.bank-rate__date'))
    ).text.strip()

    os.makedirs('screenshots', exist_ok=True)
    rate_box.screenshot('screenshots/boe_rate_verification.png')

    print(f'::set-output name=bank_rate::{current_rate}')
    print(f'::set-output name=decision_date::{decision_date}')
except Exception as e:
    print(f'::error ::Scraping failed: {str(e)}')
    print('::set-output name=bank_rate::SCRAPE_FAILED')
    print('::set-output name=decision_date::N/A')
finally:
    driver.quit()
