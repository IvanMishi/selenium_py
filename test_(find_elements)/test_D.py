import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.8/1/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Проверяет наличие чекбоксов на странице с помощью find_elements() и отмечает их, если они найдены.
    checkbox_elements = webdriver.find_elements(By.CSS_SELECTOR, ".buttons")
    # Создает пустой список для найденных элементов.
    checkbox_elements_list = []

    # Перебирает все найденные элементы
    for element in checkbox_elements:
        # Добавляет найденные элементы в список checkbox_elements_list.
        checkbox_elements_list.append(element)

    # Проверяем наличие элементов в checkbox_elements_list
    if checkbox_elements_list:
        # Определяем минимальное количество элементов для обработки из обоих списков.
        for i in range(min(len(checkbox_elements), len(checkbox_elements_list))):
            # Выполняем клик по чекбоксу
            checkbox_elements_list[i].click()
            # После клика переключается и ринимает алерт и выводит результат, если он есть.
            alert = webdriver.switch_to.alert
            alert.accept()
            result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text; print(f'Ответ: {result}') if result else None


    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
