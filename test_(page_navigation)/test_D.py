import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


with webdriver.Chrome() as webdriver:
    webdriver.get("about:blank")
    webdriver.switch_to.new_window('tab') # Запросы или поиск элементов будет выполняться на этой странице

    webdriver.get("https://parsinger.ru/selenium/8/8.1/site1/")
    num_1 = ''.join(i for i in webdriver.title if i not in ['4', '3', '9'])
    time.sleep(5)
    webdriver.get("https://parsinger.ru/selenium/8/8.1/site2/")
    num_2 = ''.join(i for i in webdriver.title if i not in ['7', '8', '0'])

    print(f'Ответ: сумма_titles {int(num_1)+int(num_2)}')