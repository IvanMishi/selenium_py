# Импортирует модуль time для работы со временем и задержками в Python
import time

# webdriver - набор команд для управления браузером
from selenium import webdriver

# импортирует класс By, выбирает способ поиска элемента
from selenium.webdriver.common.by import By

# инициализирует драйвер браузера. после этой команды увидит новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, инженер видит, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру - открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

# Метод find_element ищет нужный элемент на сайте, указав путь к нему.
# Метод принимает в качестве аргументов способ поиска и значение
# Ищет поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Пишет текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Ищет  кнопку, отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Нажимает на кнопку.
submit_button.click()
time.sleep(5)

# Закрывает окно браузера
driver.quit()
