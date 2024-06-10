# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 


# ссылка на страницу содержащую ссылку для перехода в форму регистрции
link = "http://suninjuly.github.io/find_link_text"
# переменная с мат выражением  для поиска нужной ссылки
m = str(math.ceil(math.pow(math.pi, math.e)*10000))


# для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,  использует конструкцию try/finally
# блок try используется для выполнения кода, который может вызвать исключение
try:
    # открывает браузер Chrome
    browser = webdriver.Chrome()
    # переходит по ссылке
    browser.get(link)
    # убеждается что открыта искомая страница
    time.sleep(2)


    # находит элемент на веб-странице, текст ссылки которого содержит подстроку из переменной m, и нажимает на него
    link = browser.find_element(By.PARTIAL_LINK_TEXT, m).click()

    # находит и заполняет поле input1 по названию тега
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    # находит и заполняет поле input2 по атрибуту name
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    # находит и заполняет поле input3 по значению атрибута class
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")

    # находит и заполняет поле input4 по if элемента 
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # находит элемент кнопку с помощью правил на основе CSS и нажимает на нее
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # получает alert на веб-странице
    alert = browser.switch_to.alert
    # сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # ждет 2 секунды
    time.sleep(2)
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
    # выводит значение переменной actual_result в консоль
    print('Ответ', actual_result)


# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла
