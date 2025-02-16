import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

options = {'proxy': {
    'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
    'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
    }}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as webdriver:
    webdriver.get(url)
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)