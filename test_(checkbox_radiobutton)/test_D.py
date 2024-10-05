import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.5/3/1.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Инициализация переменной для хранения общего значения textarea
    total = 0
    # Инициализация переменной для хранения общего количества найденых  отмеченых чекбоксов
    numbers = 0

    # Находит все родительские элементы на странице, содержащие чекбокс и числа в "textarea"
    parent_elements = webdriver.find_elements(By.CSS_SELECTOR, ".parent")

    # Перебирает каждый найденный элемент в списке родительских элементов
    for parent_element in parent_elements:
        # Находит textarea внутри каждого родительского элемента
        textarea_element = parent_element.find_element(By.TAG_NAME, "textarea")
        # Находит чекбокс внутри каждого родительского элемента
        checkbox_element = parent_element.find_element(By.CLASS_NAME, "checkbox")

        # Проверяет, выбран ли чекбокс
        if checkbox_element.is_selected():
            # Если чекбокс выбран, получает текст из textarea, преобразует его в число и добавляет к общей сумме
            total += int(textarea_element.text)
            # Если чекбокс выбран, добавляет количестов в переменную
            numbers += 1

            # Выводит общую сумму из textarea у отмеченных чекбоксов в консоль
    print(f'Значение суммы textarea при выбранном чекбоксе: {total}, "Количество выбранных чекбоксов:"{numbers}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
