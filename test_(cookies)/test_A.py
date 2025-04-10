import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from pprint import pprint  # Модуль для "понятной печати" структур данных, таких как словари и списки.
from selenium.webdriver.common.by import By

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.2/index.html '
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.


    # Получает все куки из текущего браузера с помощью метода get_cookies() объекта webdriver
    cookies = webdriver.get_cookies()

    # Создаёт список для хранения значений куки.
    find_cookie_values = []

    # Начинаем цикл, чтобы пройтись по каждому элементу в списке cookies
    for cookie in cookies:
        print(cookie['name'])
        
        input_area = webdriver.find_element(By.ID,'phraseInput').send_keys(str(cookie['name']))
        check_button = webdriver.find_element(By.ID, 'checkButton').click()
        print(f'Ответ: {webdriver.find_element(By.ID,'result').text }')
    time.sleep(1)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")