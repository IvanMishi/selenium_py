import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


with webdriver.Chrome() as webdriver:
    webdriver.get("https://ya.ru")
    webdriver.execute_script('window.open("https://icloud.com", "_blank");') # Открытие вкладки через JavaScript.
    time.sleep(5)
    print(webdriver.title)
    webdriver.get("https:google.com")
    time.sleep(5)
    print(webdriver.title)
    time.sleep(5)