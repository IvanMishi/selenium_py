import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.9/4/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)

    time.sleep(1) # Убеждается что открыта искомая страница

    # Ожидает
    element_ad_close = webdriver.find_element(By.CLASS_NAME, 'close').click()
    element_ad = webdriver.find_element(By.ID, 'ad')
    # убеждается что элемент больше не  видим
    if WebDriverWait(webdriver, 10).until(EC.invisibility_of_element_located((By.ID, 'ad'))):
        button = webdriver.find_element(By.TAG_NAME, 'button').click()
        print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`