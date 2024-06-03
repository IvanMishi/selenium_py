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
link = "http://suninjuly.github.io/get_attribute.html"


# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

 
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
# извлекает текстовое содержимое найденного элемента
    x = x_element.get_attribute("valuex")

    y = calc(x)


    input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    input1.send_keys(y)

    check1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    check1.click()

    radio1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio1.click()

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()

  
    # получает alert на веб-странице
    alert = browser.switch_to.alert
    # сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # ждет 2 секунды
    time.sleep(2)
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
    print('Ответ', actual_result)
    # браузер закроется автоматически после завершения блока `with`

# не забываем оставить пустую строку в конце файла
