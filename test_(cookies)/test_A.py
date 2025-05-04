import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from pprint import pprint  # Модуль для "понятной печати" структур данных, таких как словари и списки.


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.1/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'


    print('Получает все куки из текущего браузера с помощью метода get_cookies()')
    cookies = driver.get_cookies()

    print('Создаёт список для хранения значений куки.')
    find_cookie_values = []

    print('Проходит в цикле по каждому элементу в списке cookies')
    for cookie in cookies:
        # Проверяет, равняется ли имя текущего куки строке "token_22"
        if 'token_22' in cookie['name']:
            print('Добавляет значение куки по ключу в список.')
            find_cookie_values.append(cookie['value'])

            print('Выводит значения куки в качестве ответа в консоль.')
            print(f"Ответ: {cookie['value']}")


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
