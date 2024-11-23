import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.7/3/index.html'
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Инициализируем пустой список для хранения обработанных элементов ввода.
list_input = []

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Начинает бесконечный цикл.
    while True:
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags.
        input_tags = [x for x in webdriver.find_elements(By.TAG_NAME, 'input')]

        # Обходит каждый элемент input в списке.
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее.
            if tag_input not in list_input:
                # Прокручивает до элемента.
                webdriver.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                # Кликает на элемент.
                tag_input.click()
                # Добавляет элемент в список обработанных элементов.
                list_input.append(tag_input)
                
                # Выходит из цикла, если количество обработанных элементов достигло 40.
                if len(list_input) == 40:
                    break
        # Проверяет, достигло ли количество обработанных элементов 40, и выходит из внешнего цикла.
        if len(list_input) == 40:
            print(f'{len(list_input)} из {len(input_tags)} чекбоксов были отмечены')
            break
# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`

