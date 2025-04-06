import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
import re

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.5.3/index.html'
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница

    total_price = []

    load_products_button = webdriver.find_element(By.ID, 'showProducts').click()

    # Ждет, пока все элементы станут видимыми
    elements = WebDriverWait(webdriver, 60).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'price')))

    # Выводим текст каждого найденного элемента
    for element in elements:
        # Извлекает текст элемента
        text = element.text
        # Находит все цифры с помощью регулярного выражения
        numbers = re.findall(r'\d+', text)
        # Если найдено хотя бы одно число, добавляем его в список
        if numbers:
            # Объединяем все найденные числа в одну строку и добавляем в список
            total_price.append(''.join(numbers))
    # Преобразуем элементы списка в числа и вычисляем сумму
    total_sum = sum(map(int, total_price))
    # Выводим общую сумму
    print(total_sum)
    verification_form_area = webdriver.find_element(By.ID,'sumInput').send_keys(total_sum)
    check_button = webdriver.find_element(By.ID,'checkSum').click()

    print(f'Ответ: {webdriver.find_element(By.ID, 'passwordBlock').text}')
    time.sleep(1)

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")