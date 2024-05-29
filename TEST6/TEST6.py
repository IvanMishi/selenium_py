# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 

# функция с мат выражением  для заполнения поля ввода рассчитывает логарифм натуральный от модуля произведения 12 и синуса от целочисленного значения x. 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# ссылка на страницу
link = "https://suninjuly.github.io/math.html"


# для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, использует конструкцию try/finally
# блок try используется для выполнения кода, который может вызвать исключение
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

# извлекает текстовое содержимое найденного второго элемента с классом nowrap, который является потомком элемента с классом form-group 
    x_element = browser.find_element(By.CSS_SELECTOR, "[class='form-group'] .nowrap:nth-child(2)").text
# полученный текст использует в функции calc, которая преобразует текст в число, вычисляет результат и возвращает его строковое представление. Затем результат сохраняется в переменную y.
    y = calc(x_element)


# заполняет поле ввода текста на веб-странице данными из переменной y: ищет элемент <input> с классом form-control, который находится внутри элемента <div> с классом form-group, который в свою очередь является потомком элемента <div> с классом container
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.container div.form-group input.form-control')
    input1.send_keys(y)

# отмечает чекбокс на веб-странице: ищет элемент <input> с атрибутом type равным checkbox, который является потомком элемента с классом form-check
    check1 = browser.find_element(By.CSS_SELECTOR, "div.form-check [type='checkbox']")
    check1.click()

# выбирает радиокнопку на веб-странице: ищет элемент <input>, который имеет атрибут name со значением ruler и атрибут value со значением robots
    radio1 = browser.find_element(By.CSS_SELECTOR, "[name='ruler'][value='robots']")
    radio1.click()
    
# нажимает кнопку отправки формы на веб-странице: ищет элемент <input> с атрибутом type равным submit, который является прямым потомком элемента <form>
    button1 = browser.find_element(By.CSS_SELECTOR, "form > [type='submit']")
    button1.click()


# код внутри блока finally будет выполнен в любом случае
finally:
    # успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()
    print(y)

# оставляет пустую строку в конце файла
