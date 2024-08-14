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
    webdriver.set_window_size(555,  555)
    # Получает размера всего окна браузера (включая панели)
    window_size = webdriver.get_window_size()
    # Размер окна
    window_width = window_size['width']
    window_height = window_size['height']
    # Получает размер самой страницы
    viewport_size = webdriver.execute_script("""
        return {
            width: window.innerWidth,
            height: window.innerHeight
        };
    """)
    # Получает размер области просмотра (viewport)
    viewport_width = viewport_size['width']
    viewport_height = viewport_size['height']
    # Рассчитывает размер панели управления браузера
    panel_height = window_height - viewport_height
    panel_width = window_width - viewport_width


    print(f"Размер всего окна браузера: {window_width}px x {window_height}px")
    print(f"Размер области просмотра (viewport) без учета панелей управления: {viewport_width}px x {viewport_height}px")
    print(f"Размер панели управления: {panel_width}px x {panel_height}px")
    print(f"Размер окна браузера учитывая интерфейсные элементы: {window_width+panel_width}px x {window_height+panel_height}px")
    
    # Проверка, отличаются ли размеры видимой области от размеров окна браузера
    if viewport_width != window_width or viewport_height != window_height:
        # Установка нового размера окна браузера, включая размеры панелей управления
        webdriver.set_window_size(window_width + panel_width, window_height + panel_height)


    time.sleep(2)
    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.CSS_SELECTOR, "#result").text}')

    # Измеряет время выполнения кода и выводит его в консоль.
    print(f'Time is running {time.time() - start}')
