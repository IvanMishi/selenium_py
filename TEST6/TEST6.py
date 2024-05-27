# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 

# функция с мат выражением  для 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# ссылка на страницу
link = "https://suninjuly.github.io/math.html"


# для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,  использует конструкцию try/finally
# блок try используется для выполнения кода, который может вызвать исключение
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

# Использует порядковый номер дочернего элемента    
    x_element = browser.find_element(By.CSS_SELECTOR, "[class='form-group'] .nowrap:nth-child(2)").text
    y = calc(x_element)


# Использует потомков . 3 вложенности
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.container div.form-group input.form-control')
    input1.send_keys(y)

# Использует потомков . 2 вложенности
    check1 = browser.find_element(By.CSS_SELECTOR, "div.form-check [type='checkbox']")
    check1.click()
# Использует 2 фильтра 
    radio1 = browser.find_element(By.CSS_SELECTOR, "[name='ruler'][value='robots']")
    radio1.click()
    
# Использует дочерний элемент >
    button1 = browser.find_element(By.CSS_SELECTOR, "form > [type='submit']")
    button1.click()


# код внутри блока finally будет выполнен в любом случае
finally:
    # успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла
