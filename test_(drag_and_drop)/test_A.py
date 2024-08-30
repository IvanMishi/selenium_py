import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).

# Ссылка на страницу
link = 'https://parsinger.ru/draganddrop/1/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Находит элемент, который будем перетаскивать
    drag = webdriver.find_element(By.ID, "draggable")
    # Находит элемент, на который необходимо перетащить элемент element_1
    drop = webdriver.find_element(By.ID, "field2")

    # Выполняет операцию перетаскивания element_1 на элемент element_2 с использованием ActionChains
    ActionChains(webdriver).drag_and_drop(drag, drop).perform()
    # Визуально убеждается, что элемент был перетащен
    time.sleep(1)

    # Находит элемент с результатом по его ID и выводим его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'result').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`
