import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).


# Ссылка на страницу.
link = 'https://parsinger.ru/draganddrop/2/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.

    # Находит элементы перемещения элемента из одной позиции в другую.
    drag_box = webdriver.find_element(By.ID, "draggable")
    drop_boxs = webdriver.find_elements(By.CLASS_NAME, "box")

    # Выполняет операции перемещения элемента по блокам.
    for drop in drop_boxs:
        ActionChains(webdriver).drag_and_drop(drag_box, drop).perform()
    time.sleep(1) # Визуально убеждается, что элементы были перемещены

    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
