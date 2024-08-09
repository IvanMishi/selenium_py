# Импортирует необходимые библиотеки для работы с Selenium и ожиданиями
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Используемт контекстный менеджер для автоматического закрытия драйвера после выполнения действий
with webdriver.Chrome() as webdriver:
    # Открывает веб-страницу по указанному URL
    webdriver.get("https://parsinger.ru/draganddrop/1/index.html")
    # Убеждается что открыта искомая страница
    time.sleep(1)
    # Находит элемент, который будем перетаскивать
    element_1 = webdriver.find_element(By.ID, "draggable")
    # Находит элемент, на который необходимо перетащить элемент element_1
    element_2 = webdriver.find_element(By.ID, "field2")
    # Выполняет операцию перетаскивания element_1 на элемент element_2 с использованием ActionChains
    ActionChains(webdriver).drag_and_drop(element_1, element_2).perform()
    # Визуально проверяет, что элемент был перетащен 
    time.sleep(1)
    # Находит элемент с результатом по его ID и выводим его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'result').text}')