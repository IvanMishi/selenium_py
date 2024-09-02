import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.10/4/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.

    # Находит элементы для перемещения и броска в область.
    drag_boxs = webdriver.find_elements(By.CLASS_NAME, "ball_color")
    drop_boxs = webdriver.find_elements(By.CLASS_NAME, "basket_color")

    # Выполняет операции перемещения элементов в область по цвету.
    for drag in drag_boxs:
        drag_class = drag.get_attribute("class") # Получает класс элемента, чтобы определить его цвет.
        for drop in drop_boxs:
            drop_class = drop.get_attribute("class") # Получает класс целевого элемента.
            if 'red' in drag_class and 'red' in drop_class: # Проверяет, совпадают ли цвета перетаскиваемого и целевого элемента.
                ActionChains(webdriver).drag_and_drop(drag, drop).perform()
            elif 'blue' in drag_class and 'blue' in drop_class:
                ActionChains(webdriver).drag_and_drop(drag, drop).perform()
            elif 'green' in drag_class and 'green' in drop_class:
                ActionChains(webdriver).drag_and_drop(drag, drop).perform()
            elif 'black' in drag_class and 'black' in drop_class:
                # Выполняет действие перетаскивания элемента в целевую область
                ActionChains(webdriver).drag_and_drop(drag, drop).perform()
    time.sleep(1) # Визуально убеждается, что элементы были перемещены

    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.CLASS_NAME, 'message').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
