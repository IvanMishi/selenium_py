import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'http://parsinger.ru/window_size/1/'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Устанавливает размер окна баузера
    webdriver.set_window_size(555, 555)
    # Получает размеры всего окна браузера (включая панели интерфейса)
    window_size = webdriver.get_window_size()
    # Извлекает ширину и высоту окна браузера
    window_width = window_size['width']
    window_height = window_size['height']
    # Получает размер самой страницы (viewport)
    viewport_size = webdriver.execute_script("""return {width: window.innerWidth,height: window.innerHeight};""")
    # Извлекает ширину и высоту области просмотра (viewport)
    viewport_width = viewport_size['width']
    viewport_height = viewport_size['height']
    # Рассчитывает размеры панелей управления браузера
    panel_height = window_height - viewport_height
    panel_width = window_width - viewport_width

    print(f"Размер всего окна браузера: {window_width}px x {window_height}px")
    print(f"Размер области просмотра (viewport) без учета панелей управления: {viewport_width}px x {viewport_height}px")
    print(f"Размер панели управления: {panel_width}px x {panel_height}px")
    print(
        f"Размер окна браузера учитывая интерфейсные элементы: {window_width + panel_width}px x {window_height + panel_height}px")

    # Проверка, отличаются ли размеры видимой области от размеров окна браузера
    if viewport_width != window_width or viewport_height != window_height:
        # Установка нового размера окна браузера, включая размеры панелей управления
        webdriver.set_window_size(window_width + panel_width, window_height + panel_height)

    time.sleep(1)
    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.CSS_SELECTOR, "#result").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`