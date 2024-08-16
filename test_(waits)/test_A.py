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
link = 'http://parsinger.ru/expectations/3/index.html'
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Список для хранения результата
result = []

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Ожидает 5 сек пока кнопка на странице не станет активной и нажимает на нее если она кликабельна
    button = WebDriverWait(webdriver, 5).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    # Ожидает точного совпадения заголовка, если заголово совпадает выводит текст из элемента с id='result' в консоль
    if WebDriverWait(webdriver, 30).until(EC.title_is('345FDG3245SFD')):

        print(f'Ответ:{webdriver.find_element(By.ID, "result").text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла