import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'http://parsinger.ru/window_size/2/index.html'
#Значения ширины и высоты окна браузера
window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Цикл по диапазону значений ширины окна.
    for x in window_size_x:
        # Цикл по диапазону значений высоты окна.
        for y in window_size_y:
            # Ширина равна x, высота вычисляется как 139 плюс текущее значение y.
            # Получаем текущий размер окна и сохраняем его в переменной window_size
            window_size = webdriver.get_window_size()
            # Извлекает ширину и высоту окна браузера
            window_width = window_size['width']
            window_height = window_size['height']
            # Получает размер самой страницы (viewport)
            viewport_size = webdriver.execute_script(
                """return {width: window.innerWidth,height: window.innerHeight};""")
            # Извлекает ширину и высоту области просмотра (viewport)
            viewport_width = viewport_size['width']
            viewport_height = viewport_size['height']
            # Рассчитывает размеры панелей управления браузера
            panel_height = window_height - viewport_height
            panel_width = window_width - viewport_width
            webdriver.set_window_size(x, panel_height + y) # нужно задать размер с учетом панелей браузера вместо 139



            # print(f'{x}x{y} --- {window_size["width"]}x{window_size["height"]}')
            # Находит элемент на странице с id "result" и извлекаем его текст
            result = webdriver.find_element('xpath', '//span[@id="result"]').text
            # Если результат не пустой, выводим его в консоль с указанием разрешения окна
            if result:
                print(f'Ответ: {result} в разрешении {{\'width\': {x}, \'height\': {y}}}')



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`