import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# ссылка на страницу
link = "https://parsinger.ru/selenium/5.5/2/1.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.


    # Ищет все элементы ввода (input) на странице с использованием метода find_elements
    input_elements = webdriver.find_elements(By.TAG_NAME, "input")

    # Перебирает каждый найденный элемент input
    for element in input_elements:
        # Проверяет, не отключен ли элемент с помощью атрибута 'disabled'
        if not element.get_attribute('disabled'):
            # Если элемент не отключен, очищает его содержимое
            element.clear()
    # Находиn кнопку для проверки и нажимает на нее
    check_button = webdriver.find_element(By.ID, "checkButton").click()

    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(f'Ответ: {actual_result}')
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
