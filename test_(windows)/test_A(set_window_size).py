# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# Ссылка на страницу
link = "http://parsinger.ru/window_size/1/"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Устанавливает размер окна баузера
    webdriver.set_window_size(555, 139 + 555)
    # Убеждается что открыта искомая страница
    time.sleep(1)
    #  # Находит элемент с результатом по его ID и выводит его текст
    result = webdriver.find_element(By.CSS_SELECTOR, "#result").text
    print(f'Ответ: {result}')
    # Выводит ширину и высоту браузера в консоль
    print(f'Ширина: {webdriver.get_window_size().get('width')} Высота: {webdriver.get_window_size().get('height')}')

    # Измеряет время выполнения кода и выводит его в консоль.
    print(f'Time is running {time.time() - start}')
