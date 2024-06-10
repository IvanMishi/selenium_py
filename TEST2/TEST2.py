# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# ссылка на страницу
link = "http://suninjuly.github.io/simple_form_find_task.html"

# блок try используется для выполнения кода, который может вызвать исключение
try:
    # открывает браузер Chrome
    browser = webdriver.Chrome()
    # переходит по ссылке
    browser.get(link)
    # находит и заполняем поле input1
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    # находит и заполняем поле input2
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    # находит и заполняем поле input3
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    # находит и заполняем поле input4
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    # находит и нажимает кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

# получает alert на веб-странице
    alert = browser.switch_to.alert
    # сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
# выводит значение переменной actual_result в консоль
    print('Ответ', actual_result)

# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    browser.quit()

# не забывает оставить пустую строку в конце файла
