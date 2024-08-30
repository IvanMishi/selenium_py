# Импортирует необходимые библиотеки для работы с Selenium и ожиданиями
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains

# Используемт контекстный менеджер для автоматического закрытия драйвера после выполнения действий
with webdriver.Chrome() as webdriver:
    # Открывает веб-страницу по указанному URL
    webdriver.get('https://parsinger.ru/selenium/5.10/3/index.html')
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Находит элементы: которые будет перетаскивать и куда будет перетаскивать
    drag_elements = webdriver.find_elements(By.CLASS_NAME, 'draganddrop')
    drop_elements = webdriver.find_elements(By.CLASS_NAME, 'draganddrop_end')

    # Действия с перетаскиванием элементов
    for drag, drop in zip(drag_elements, drop_elements):
        if Color.from_string(drag.value_of_css_property('background-color')).rgb == Color.from_string(drop.value_of_css_property('border-color')).rgb:
            ActionChains(webdriver).click_and_hold(drag).move_to_element(drop).release().perform()
            time.sleep(.1)
            
    time.sleep(1)
            # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')
