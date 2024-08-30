import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).
from selenium.webdriver.support.color import Color # Импортирует класс Color для работы с цветами в веб-элементах.


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.10/3/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Находит элементы: которые будет перетаскивать и куда будет перетаскивать
    drag_elements = webdriver.find_elements(By.CLASS_NAME, 'draganddrop')
    drop_elements = webdriver.find_elements(By.CLASS_NAME, 'draganddrop_end')

    # Действия с перетаскиванием элементов
    for drag, drop in zip(drag_elements, drop_elements):
        if Color.from_string(drag.value_of_css_property('background-color')).rgb == Color.from_string(
                drop.value_of_css_property('border-color')).rgb:
            ActionChains(webdriver).click_and_hold(drag).move_to_element(drop).release().perform()
            time.sleep(.1)

    time.sleep(1)
    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`
