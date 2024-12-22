import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from pprint import pprint  # Модуль для "понятной печати" структур данных, таких как словари и списки.


# Ссылка на страницу.
link = 'https://parsinger.ru/methods/3/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Инициализирует переменную total значением 0 для накопления суммарного значения куки
    total = 0
    # Получает все куки из текущего браузера с помощью метода get_cookies() объекта webdriver
    cookies = webdriver.get_cookies()


    # Начинаем цикл, чтобы пройтись по каждому элементу в списке cookies
    for cookie in cookies:
    # Извлекает числовую часть из имени куки
        digit = ''.join(filter(str.isdigit, cookie['name']))
    # Проверяет, является ли извлеченная цифра четной
        if int(digit) %2 ==0:
    # Добавляет числовое значение, связанное с куки, к общему количеству
            total = total + int(cookie['value'])
    # Выводит итоговую сумму
    print(f"Ответ: {total}")


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`