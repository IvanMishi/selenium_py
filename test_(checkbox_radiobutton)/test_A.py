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

# Функция с мат выражением для заполнения поля ввода рассчитывает логарифм натуральный от модуля произведения 12 и синуса от целочисленного значения x. 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Ссылка на страницу
link = "http://suninjuly.github.io/get_attribute.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
# Открывает браузер Chrome
with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

 
    x_element = webdriver.find_element(By.CSS_SELECTOR, "[id='treasure']")
    # извлекает текстовое содержимое найденного элемента
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    # Заполняет поле ввода текста на веб-странице данными из переменной y
    input_area = webdriver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(y)
    # Отмечает чекбокс на веб-странице
    checkbox = webdriver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    # Выбирает радиокнопку на веб-странице
    radio_button = webdriver.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    # Нажимает кнопку отправки формы на веб-странице
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла