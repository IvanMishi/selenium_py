import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')

with webdriver.Chrome(options=options_chrome) as webdriver:
    webdriver.get(url)
    time.sleep(1)
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(1)
