import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.5.2/index.html'
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница


    WebDriverWait(webdriver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'button'))).click()
    print(f'Ответ: {webdriver.find_element(By.ID, 'password-display').text.split(":")[1].strip()}')
    time.sleep(1)

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")