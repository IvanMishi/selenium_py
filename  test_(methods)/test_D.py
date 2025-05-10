import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/selenium/5.5/2/1.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Ищет все элементы ввода input() на странице с используя метод find_elements')
    input_elements = driver.find_elements(By.TAG_NAME, "input")

    print('Перебирает каждый найденный элемент input()')
    for element in input_elements:
        # Проверяет, не отключен ли элемент с помощью атрибута "disabled".
        if not element.get_attribute('disabled'):
            # Если элемент не отключен, очищает его содержимое
            element.clear()
    print('Находиn кнопку для проверки и нажимает на нее')
    check_button = driver.find_element(By.ID, "checkButton").click()

    print('Получает alert на веб-странице')
    alert = driver.switch_to.alert
    print('Сохраняет текст предупреждения (alert) в переменной actual_result')
    actual_result = alert.text
    print('Выводит числовое значение полученного текста из alert в консоль в качестве ответа')
    print(f'Ответ: {actual_result}')
    print('Принимает и закрывает alert путем нажатия кнопки "OK" (accept)')
    alert.accept()


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
