# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re

# Ссылка на страницу
link = "http://suninjuly.github.io/simple_form_find_task.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Находит и заполняет поле First name
    input_first_name = webdriver.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    # Находит и заполняет поле Last name
    input_last_name = webdriver.find_element(By.NAME, "last_name").send_keys("Petrov")
    # Находит и заполняет поле City
    input_сity = webdriver.find_element(By.CLASS_NAME, "form-control.city").send_keys("Smolensk")
    # Находит и заполняет поле Country
    input_сountry = webdriver.find_element(By.ID, "country").send_keys("Russia")
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
