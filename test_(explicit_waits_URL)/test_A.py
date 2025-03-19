import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.4.3/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Находит элемент на веб-странице с текстом ссылки, содержащим подстроку 'Правильный путь', и нажимает на него.
    correct_way_button = webdriver.find_element(By.LINK_TEXT, 'Правильный путь').click()

    # Ожидает смены ссылки на странице.
    change_url = WebDriverWait(webdriver, 10).until(EC.url_to_be("https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"))
    # Если ссылка изменилась на ожидаемую, ждет появления элемента с паролем, и выводит из него текст в качестве ответа.
    if change_url:
        print(f'Ответ: {WebDriverWait(webdriver,10).until(EC.visibility_of_element_located((By.ID, 'password'))).text}')


    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
