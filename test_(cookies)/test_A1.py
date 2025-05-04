import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from pprint import pprint  # Модуль для "понятной печати" структур данных, таких как словари и списки.

# Ссылка на страницу.
link = 'https://parsinger.ru/methods/3/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'


    print('Инициализирует переменную total значением 0 для накопления суммарного значения куки.')
    total = 0
    print('Получает все куки из текущего браузера с помощью метода get_cookies() объекта webdriver')
    cookies = driver.get_cookies()

    print('Создаёт список для хранения значений куки.')
    secret_cookie_name = []
    secret_cookie_values = []

    print('Проходит в цикле по каждому элементу в списке cookies')
    for cookie in cookies:
        # Проверяет, содержит ли имя текущего куки подстроку 'secret_cookie_'.
        if 'secret_cookie_' in cookie['name']:
            # Если да, то добавляет к общей сумме значение этого куки, преобразуя его в целое число.
            total = total + int(cookie['value'])
            # Добавляет значение куки по ключу в список.
            secret_cookie_name.append(cookie['name'])
            secret_cookie_values.append(cookie['value'])

            print('Выводим имя и значение куки в консоль.')
            name = cookie['name']  # Получает имя куки.
            value = cookie['value']  # Получает значение куки.
            print(f"Имя: {name}, Значение: {value}")

    print('Выводит итоговую сумму значений всех куки, которые имели название с подстрокой "secret_cookie_"')
    print(f'Общая сумма значениий куки: {total}')
    print('Все куки в виде словаря:')
    pprint(cookies)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")