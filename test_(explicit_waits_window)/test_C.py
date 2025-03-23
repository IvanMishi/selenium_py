import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.7.3/index.html'
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница


    summon_button = webdriver.find_element(By.ID, 'summonBtn').click()
    window_handle = webdriver.current_window_handle



    if WebDriverWait(webdriver, 10).until(EC.number_of_windows_to_be(5)):  # Ожидаем, пока не откроется новое окно
        pass_button = webdriver.find_element(By.ID, 'passwordBtn').click()
        # Ожидает, что модальное окно появится, переключается на него и выводит число из текста в консоль в качестве ответа
        print(f'Ответ {WebDriverWait(webdriver, 60).until(EC.alert_is_present()).text.split(":")[1].strip()}')
        webdriver.switch_to.window(window_handle)
        webdriver.switch_to.alert.accept()



    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

