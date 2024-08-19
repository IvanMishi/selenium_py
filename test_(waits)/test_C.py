# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Ссылка на страницу
link = 'https://parsinger.ru/expectations/6/index.html'
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Ожидает 5 сек пока кнопка на странице не станет активной и нажимает на нее если она кликабельна
    button = WebDriverWait(webdriver, 5).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    time.sleep(1)
    # Ожидает появления элемента с class='BMH21YY' и выводит из него текст в качестве ответа
    print(f'Ответ:{WebDriverWait(webdriver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))).text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла
