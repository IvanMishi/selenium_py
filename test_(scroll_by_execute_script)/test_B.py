import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу
link = "http://parsinger.ru/scroll/2/"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Список для хранения результата
result = []

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит все чекбоксы и span элементы на странице.
    input_list = webdriver.find_elements(By.TAG_NAME, 'input')
    span_list = webdriver.find_elements(By.TAG_NAME, 'span')

    # Прокручивает к каждому чекбоксу и кликает на него
    for checkbox, span in zip(input_list, span_list):
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()
        if span.text.isdigit(): # Ищет цифры в тексте.
            result.append(int(span.text)) # Найденные цифры добавляет в список 'result'


    # Выводит сумму всех чисел, найденных в элементах span в консоль
    print(f'Ответ: {sum(result)}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`