import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://2ip.ru/'
with webdriver.Chrome() as webdriver:
    webdriver.get(url)
    time.sleep(1)
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(1)