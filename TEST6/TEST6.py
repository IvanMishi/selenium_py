# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# Импортирует модуль math, который предоставляет математические функции
import math
# Импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re


# Функция с мат выражением  для заполнения поля ввода рассчитывает логарифм натуральный от модуля произведения 12 и синуса от целочисленного значения x. 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Ссылка на страницу
link = "https://suninjuly.github.io/math.html"


# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Извлекает текстовое содержимое найденного второго элемента с классом nowrap, который является потомком элемента с классом form-group 
    x_element = webdriver.find_element(By.CSS_SELECTOR, "[class='form-group'] .nowrap:nth-child(2)").text
    # Полученный текст использует в функции calc, которая преобразует текст в число, вычисляет результат и возвращает его строковое представление. Затем результат сохраняется в переменную y.
    y = calc(x_element)

    # Заполняет поле ввода текста на веб-странице данными из переменной y: ищет элемент <input> с классом form-control, который находится внутри элемента <div> с классом form-group, который в свою очередь является потомком элемента <div> с классом container
    input_area = webdriver.find_element(By.CSS_SELECTOR, 'div.container div.form-group input.form-control').send_keys(y)

    # Отмечает чекбокс на веб-странице: ищет элемент <input> с атрибутом type равным checkbox, который является потомком элемента с классом form-check
    checkbox = webdriver.find_element(By.CSS_SELECTOR, "div.form-check [type='checkbox']").click()

    # Выбирает радиокнопку на веб-странице: ищет элемент <input>, который имеет атрибут name со значением ruler и атрибут value со значением robots
    radio_button = webdriver.find_element(By.CSS_SELECTOR, "[name='ruler'][value='robots']").click()
    
    # Нажимает кнопку отправки формы на веб-странице: ищет элемент <input> с атрибутом type равным submit, который является прямым потомком элемента <form>
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "form > [type='submit']").click()

# Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа

except ValueError as e:
    print(f"Произошла ошибка при обработке значений на веб-странице: {e}")

# Код внутри блока finally будет выполнен в любом случае
finally:
    # Закрывает браузер
    webdriver.quit()

# Не забывает оставить пустую строку в конце файла
