# Импортирует необходимые библиотеки для работы с Selenium и ожиданиями
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Используемт контекстный менеджер для автоматического закрытия драйвера после выполнения действий
with webdriver.Chrome() as webdriver:
    # Открывает веб-страницу по указанному URL
    webdriver.get("https://parsinger.ru/draganddrop/3/index.html")
    # Убеждается что открыта искомая страница
    time.sleep(1)
    # Находит элемент, для перемещения
    drag = webdriver.find_element(By.ID, "block1")
    # Находит элемент, на который перемесщает
    controlPoints = webdriver.find_elements(By.CLASS_NAME, "controlPoint")
    # Выполняет операцию захвата и удержания элемента
    ActionChains(webdriver).click_and_hold(drag).perform()
    # Выполняет операцию перемещения удерживаемого элемента в цикле по контрольным точкам
    for point in controlPoints:
        ActionChains(webdriver).move_to_element(point).perform()
    #Выполняет оерацию отпускания удерживаемого элемента после перемещения по контролным точкам
    ActionChains(webdriver).release(drag).perform()

    # Визуально убеждается, что элемент был перемещен
    time.sleep(1)

    # Находит элемент с результатом по его ID и выводим его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')
