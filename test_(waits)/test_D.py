# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.9/2/index.html'
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)
    # Ожидает 60 сек пока блок с id ='qQm9y1rk' появится на странице и нажимает на него
    element = WebDriverWait(webdriver, 60).until(EC.presence_of_element_located((By.ID, "qQm9y1rk"))).click()
    print(webdriver.switch_to.alert.text)

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла
