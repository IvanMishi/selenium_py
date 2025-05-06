import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/methods/3/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Инициализирует переменную total значением 0 для накопления суммарного значения куки')
    total = 0
    print('Получает все куки из текущего браузера с помощью метода get_cookies() объекта webdriver')
    cookies = driver.get_cookies()


    print('Начинает цикл, чтобы пройтись по каждому элементу в списке cookies')
    for cookie in cookies:
        print('Извлекает числовую часть из имени куки')
        digit = ''.join(filter(str.isdigit, cookie['name']))
        print('Проверяет, является ли извлеченная цифра четной')
        if int(digit) %2 ==0:
            print('Добавляет числовое значение, связанное с куки, к общему количеству')
            total = total + int(cookie['value'])
    print('Выводит итоговую сумму в качестве ответа')
    print(f"Ответ: {total}")


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`