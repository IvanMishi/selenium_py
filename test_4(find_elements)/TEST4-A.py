# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# Импортирует модуль math, который предоставляет математические функции
import math
# Импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re


# Ссылка на страницу 
link = "http://suninjuly.github.io/huge_form.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)
    
    # Поиск внутри списка элементов: находит все элементы на странице, которые являются элементами ввода (input) c помощью метода find_elements()
    input_elements = webdriver.find_elements(By.TAG_NAME, "input")
    # Пребирает каждый найденный элемент в списке input_elements
    for element in input_elements:
    # Вводит текст "Мой ответ" в каждый элемент ввода
        element.send_keys("Ответ")
        
    # Находит и нажимает кнопку Submit
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "button.btn").click()


    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# Код внутри блока finally будет выполнен в любом случае
finally:
    # Измеряет время выполнения кода и выводит его в консоль.
    print(f'Time is running {time.time() - start}')
    # Закрывает браузер
    webdriver.quit()

# Не забывает оставить пустую строку в конце файла