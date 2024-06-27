# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math
# импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам. 
import re


# ссылка на страницу содержащую ссылку для перехода в форму регистрции
link = "http://suninjuly.github.io/find_link_text"
# переменная с мат выражением  для поиска нужной ссылки
m = str(math.ceil(math.pow(math.pi, math.e)*10000))


# для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,  использует конструкцию try/finally
# блок try используется для выполнения кода, который может вызвать исключение
try:
    # открывает браузер Chrome
    driver = webdriver.Chrome()
    # переходит по ссылке
    driver.get(link)
    # убеждается что открыта искомая страница
    time.sleep(2)


    # находит элемент на веб-странице, текст ссылки которого содержит подстроку из переменной m, и нажимает на него
    link = driver.find_element(By.PARTIAL_LINK_TEXT, m).click()

    # находит и заполняет поле input1 по названию тега
    input1 = driver.find_element(By.TAG_NAME, "input").send_keys("Ivan")

    # находит и заполняет поле input2 по атрибуту name
    input2 = driver.find_element(By.NAME, "last_name").send_keys("Petrov")

    # находит и заполняет поле input3 по значению атрибута class
    input3 = driver.find_element(By.CLASS_NAME, "form-control.city").send_keys("Smolensk")

    # находит и заполняет поле input4 по if элемента 
    input4 = driver.find_element(By.ID, "country").send_keys("Russia")

    # находит элемент кнопку с помощью правил на основе CSS и нажимает на нее
    button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    # получает alert на веб-странице
    alert = driver.switch_to.alert
    # выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    driver.quit()

# оставляет пустую строку в конце файла
