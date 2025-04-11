import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import math  # Модуль для выполнения математических расчетов
import re  # Модуль для работы с регулярными выражениями


# Ссылка на страницу
link = "https://parsinger.ru/selenium/8/8.2.2/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with (webdriver.Chrome() as driver):  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'  # Ошибка будет выведена в консоль в случае если URL не совпадают

    print(driver.get_window_size()["width"]) # Ширина окна браузера.
    print(driver.get_window_size()["height"])  # Высота окна браузера.
    sumx = (driver.get_window_size()["width"] + driver.get_window_size()["height"])

    input_area = driver.find_element(By.ID,'answer').send_keys(sumx)
    button_submit = driver.find_element(By.ID,'checkBtn').click()
    time.sleep(1)

    print(f'Ответ: {driver.find_element(By.ID, 'resultMessage').text.split(":")[1].strip()}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")