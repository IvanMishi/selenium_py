import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


with webdriver.Chrome() as webdriver:
    pass
    print(webdriver.execute_script("return document.title;"))
    time.sleep(5)
    webdriver.get("about:blank")
    print(webdriver.execute_script("return document.title;"))
    time.sleep(5)
    

