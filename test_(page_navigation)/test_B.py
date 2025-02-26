import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


with webdriver.Chrome() as webdriver:
    webdriver.switch_to.new_window('tab') # Запросы или поиск элементов будет выполняться на этой странице
    webdriver.get("https://ya.ru")
    time.sleep(5)
    print(webdriver.title)
    webdriver.get("https:google.com")
    time.sleep(5)
    print(webdriver.title)
    time.sleep(5)