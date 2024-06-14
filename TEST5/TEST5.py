# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re


# ссылка на страницу 
link = "http://suninjuly.github.io/find_xpath_form"


# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае
try:
    # открывает браузер Chrome
    browser = webdriver.Chrome()
    # переходит по ссылке
    browser.get(link)

    # находит и заполняет поле input1 с помощью правил на основе X-path
    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Ivan")
    # находит и заполняет поле input2 с помощью правил на основе X-path
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Petrov")
    # находит и заполняет поле input3 с помощью правил на основе X-path
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']").send_keys("Smolensk")
    # находит и заполняет поле input4 с помощью правил на основе X-path
    input4 = browser.find_element(By.XPATH, "//input[@id='country']").send_keys("Russia") 

    # находит кнопку с помощью правил на основе X-path и нажимает на нее
    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

# получает alert на веб-странице
    alert = browser.switch_to.alert
    # выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла
