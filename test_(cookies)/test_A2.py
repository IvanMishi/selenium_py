import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from pprint import pprint  # Модуль для "понятной печати" структур данных, таких как словари и списки.

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.1/index.html'
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
        # Проверяет, содержит ли имя текущего куки подстроку 'token_22'
        if 'token_22' in cookie['name']:
            # Добавляет значение куки по ключу в список.
            find_cookie_values.append(cookie['name'])
            find_cookie_values.append(cookie['value'])

            # Выводим только значения куки в качестве ответа
            print(f"Ответ: {cookie['value']}")  # Выводит значение куки в консоль.



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
