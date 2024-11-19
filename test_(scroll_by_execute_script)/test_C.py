import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.7/3/index.html'
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Инициализируем пустой список для хранения обработанных элементов ввода.
list_input = []

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Начинаем бесконечный цикл.
    while True:
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags.
        input_tags = [x for x in webdriver.find_elements(By.TAG_NAME, 'input')]

        # Обходим каждый элемент input в списке.
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее.
            if tag_input not in list_input:
                # Скроллит до элемента.
                webdriver.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                # Кликает на элемент.
                tag_input.click()
                # Добавляет элемент в список обработанных элементов.
                list_input.append(tag_input)
                print(len(list_input), len(input_tags))
                # Выходит из цикла, если количество обработанных элементов достигло 40.
                if len(list_input) == 40:
                    break
        # Проверяет, достигло ли количество обработанных элементов 40, и выходит из внешнего цикла.
        if len(list_input) == 40:
            break

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла
