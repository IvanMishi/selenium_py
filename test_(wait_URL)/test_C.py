import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Находит кнопку на веб-странице с id'searchLink', и нажимает на него.
    searchLink_button = webdriver.find_element(By.CLASS_NAME, 'search-link')
    searchLink_button.click()

    # Ожидает подстроку в текущем URL.
    text_url = WebDriverWait(webdriver, 60).until(EC.url_contains("qLChv49"))
    # Если в URL ________ с паролем, и выводит из него текст в качестве ответа.
    while True:
        searchLink_button.click()



    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
