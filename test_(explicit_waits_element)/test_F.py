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


    try: # Ожидает появления рекламного окна
        ad_element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.ID, 'ad')))
        if ad_element: # Если рекламное окно присутствует на странице
            try:
                # Ожидаем кликабельности элемента с ID 'close' в течение 10 секунд, чтоб закрыть рекламное окно
                close_element = WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
                if close_element:
                    # Кликаем по элементу с классом 'close'
                    close_element.click()
            except TimeoutException:
                print("Элемент 'close' не найден или не кликабелен в течение заданного времени ожидания.")

        # Убеждается что рекламное окно более не видимо пользователю
        if WebDriverWait(webdriver, 10).until(EC.invisibility_of_element_located((By.ID, 'ad'))):

            button = WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
            if button:
                button.click()

    except TimeoutException:
        print("Рекламное окно с id='ad' не появилось на странице  в течение заданного времени ожидания.")
    #Выводит текст из элемента в консоль, если он станет ненулевым (не пустым).
    if WebDriverWait(webdriver, 10).until(lambda d: d.find_element(By.ID, 'message').text != ""):
        print(webdriver.find_element(By.ID, 'message').text)
        
    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`
