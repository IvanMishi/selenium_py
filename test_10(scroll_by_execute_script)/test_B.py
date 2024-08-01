# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# Ссылка на страницу
link = 'http://parsinger.ru/scroll/2/'
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Список для хранения результата
result = []

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Находит все элементы input на странице
    input_list = webdriver.find_elements(By.TAG_NAME, 'input')

    # Прокручивает к каждому элементу input и кликает на него
    for tag_input in input_list:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
        tag_input.click()
    # Находит все элементы span на странице и ищет цифры в их тексте, найденные цифры добавляет в список 'result'
    for x in webdriver.find_elements(By.TAG_NAME, 'span'):
        if x.text.isdigit():
            result.append(int(x.text))

    # Выводит сумму всех чисел, найденных в элементах span в консоль
    print(f'Ответ: {sum(result)}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла