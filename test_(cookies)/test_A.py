import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


# Ссылка на страницу.
link = 'https://parsinger.ru/methods/3/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Получает все куки из браузера
    cookies = webdriver.get_cookies()
    # Инициализируем общее количество нулем
    total = 0

    # Проходим по каждому куки
    for cookie in cookies:
        # Проверяет, содержит ли имя куки подстроку 'secret_cookie_'
        if 'secret_cookie_' in cookie['name']:
            # Увеличиваем общий итог на значение куки (приведенное к целому числу)
            total = total + int(cookie['value'])

    #total = total + int(cookie['value'])
    # Выводит итоговую сумму
    print(f'Общая сумма значениий куки: {total}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`