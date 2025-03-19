import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'http://parsinger.ru/expectations/4/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Ожидает 5 сек кликабельности кнопки на странице
    button = WebDriverWait(webdriver, 5).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    # Ожидает частичного совпадения заголовка, если заголовок частично совпадает выводит текст из элемента с id='result' в консоль
    if WebDriverWait(webdriver, 30).until(EC.title_contains('JK8HQ')):
        print(f'Ответ:{webdriver.find_element(By.ID, "result").text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`
