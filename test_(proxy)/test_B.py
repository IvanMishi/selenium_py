import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

proxy = '8.210.83.33:80'
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)