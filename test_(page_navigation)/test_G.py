import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    result = []
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/2.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/3.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/4.html")
    time.sleep(2)
    print(browser.window_handles)