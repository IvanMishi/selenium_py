import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import \
    ActionChains  # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.10/2/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    # Устанавливает размер окна при запуске браузера
    webdriver.set_window_size(1200, 900)
    webdriver.get(link)  # Переходит по ссылке
    time.sleep(1)  # Убеждается что открыта искомая страница

    # Находит элементы перемещения элемента из одной позиции в другую.
    drag_list = webdriver.find_elements(By.CLASS_NAME, "ui-draggable")
    drop_area = webdriver.find_element(By.CLASS_NAME, 'draganddrop_end')
    # Действия с перетаскиванием элементов на расстояние из разницы между шириной экрана и шириной элемента
    for element in drag_list:
        ActionChains(webdriver).drag_and_drop_by_offset(element, (
                webdriver.get_window_size()["width"] - (drop_area.size['width'])), 0).perform()
    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
