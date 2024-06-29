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


# функция с мат выражением  для заполнения поля ввода рассчитывает логарифм натуральный от модуля произведения 12 и синуса от целочисленного значения x. 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# ссылка на страницу
link = "https://suninjuly.github.io/math.html"


# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае
try:
    # открывает браузер Chrome
    driver = webdriver.Chrome()
    # переходит по ссылке
    driver.get(link)

    # извлекает текстовое содержимое найденного второго элемента с классом nowrap, который является потомком элемента с классом form-group 
    x_element = driver.find_element(By.CSS_SELECTOR, "[class='form-group'] .nowrap:nth-child(2)").text
    # полученный текст использует в функции calc, которая преобразует текст в число, вычисляет результат и возвращает его строковое представление. Затем результат сохраняется в переменную y.
    y = calc(x_element)

    # заполняет поле ввода текста на веб-странице данными из переменной y: ищет элемент <input> с классом form-control, который находится внутри элемента <div> с классом form-group, который в свою очередь является потомком элемента <div> с классом container
    input_area = driver.find_element(By.CSS_SELECTOR, 'div.container div.form-group input.form-control').send_keys(y)

    # отмечает чекбокс на веб-странице: ищет элемент <input> с атрибутом type равным checkbox, который является потомком элемента с классом form-check
    checkbox = driver.find_element(By.CSS_SELECTOR, "div.form-check [type='checkbox']").click()

    # выбирает радиокнопку на веб-странице: ищет элемент <input>, который имеет атрибут name со значением ruler и атрибут value со значением robots
    radio_button = driver.find_element(By.CSS_SELECTOR, "[name='ruler'][value='robots']").click()
    
    # нажимает кнопку отправки формы на веб-странице: ищет элемент <input> с атрибутом type равным submit, который является прямым потомком элемента <form>
    button_submit = driver.find_element(By.CSS_SELECTOR, "form > [type='submit']").click()

# получает alert на веб-странице
    alert = driver.switch_to.alert
    # выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

except ValueError as e:
    print(f"Произошла ошибка при обработке значений на веб-странице: {e}")

# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    driver.quit()

# оставляет пустую строку в конце файла
