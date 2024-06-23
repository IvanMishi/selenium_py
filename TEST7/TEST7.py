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

# функция с мат выражением для заполнения поля ввода рассчитывает логарифм натуральный от модуля произведения 12 и синуса от целочисленного значения x. 
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
    
    # заполняет поле ввода текста на веб-странице данными из переменной y
    input = browser.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(y)

    # отмечает чекбокс на веб-странице
    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()

    # выбирает радиокнопку на веб-странице
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
 
    # нажимает кнопку отправки формы на веб-странице
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # получает alert на веб-странице
    alert = browser.switch_to.alert
    # выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
    # браузер закроется автоматически после завершения блока `with`

# оставляет пустую строку в конце файла
