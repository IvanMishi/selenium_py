import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from pprint import pprint  # Модуль для "понятной печати" структур данных, таких как словари и списки.
import json # Модуль для преобразования в формат json
from selenium.webdriver.common.by import By
import re

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.6/1/index.html'
# Измеряет время выполнения.
start = time.time()

# Чтение куков из текстового файла
with open('cookie_dict.txt', 'r') as file:  # Открывает текстовый файл для чтения
    cookie_dict = json.load(file)  # Читает и загружает куки как список словарей


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Добавляет все куки из списка
    for cookie in cookie_dict:
        webdriver.delete_all_cookies()  # Удаляет все куки (это можно сделать один раз вне цикла)
        webdriver.add_cookie(cookie)  # Добавляет куку
        webdriver.refresh()  # Обновляет страницу

        skill_list = webdriver.find_elements(By.CSS_SELECTOR, "#skillsList > li")
        age = webdriver.find_element(By.ID,"age").text

        print(len(skill_list), int(re.search(r'\d+', age).group()))
        time.sleep(100)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`