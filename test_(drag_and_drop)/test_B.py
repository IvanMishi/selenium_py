import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).

# Ссылка на страницу
link = 'https://parsinger.ru/draganddrop/3/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке
    time.sleep(1) # Убеждается что открыта искомая страница

    # Находит элемент для удержания и перемещения по контрольным точкам
    drag_element = webdriver.find_element(By.ID, "block1")
    drop_element_points = webdriver.find_elements(By.CLASS_NAME, "controlPoint")

    # Выполняет операцию захвата и удержания элемента
    ActionChains(webdriver).click_and_hold(drag_element).perform()
    # Выполняет операцию перемещения удерживаемого элемента в цикле по контрольным точкам
    for point in drop_element_points:
        ActionChains(webdriver).move_to_element(point).perform()
    # Выполняет оерацию отпускания удерживаемого элемента после перемещения по контролным точкам
    ActionChains(webdriver).release(drag_element).perform()

    
    time.sleep(1) # Визуально убеждается, что элемент был перемещен
    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
 