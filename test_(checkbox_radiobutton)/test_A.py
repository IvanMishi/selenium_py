import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import math # Модуль для выполнения математических расчетов
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'http://suninjuly.github.io/get_attribute.html'
# Измеряет время выполнения.
start = time.time()

# Функция с математическим выражением вычисляет натуральный логарифм модуля произведения 12 и синуса целочисленного значения x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.

    # Находит элемент с идентификатором 'treasure', извлекает его значение из атрибута 'valuex' и вычисляет его с помощью функции calc.
    x= calc(webdriver.find_element(By.CSS_SELECTOR, "[id='treasure']").get_attribute("valuex"))

    # Заполняет поле ввода текста на веб-странице данными из переменной x
    input_area = webdriver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(x)
    # Отмечает чекбокс на веб-странице
    checkbox_button = webdriver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    # Выбирает радиокнопку на веб-странице
    radio_button = webdriver.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    # Нажимает кнопку отправки формы на веб-странице
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(1)  # Визуально убеждается, что все действия выполнены

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
    # Браузер закрывается автоматически после завершения блока `with`
