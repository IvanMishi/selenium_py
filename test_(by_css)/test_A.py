import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import re # Модуль для работы с регулярными выражениями
import math

# Ссылка на страницу
link = "https://suninjuly.github.io/math.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
def calc(x): # Функция рассчитывает натуральный логарифм модуля произведения 12 и синуса целочисленного значения x.
  return str(math.log(abs(12*math.sin(int(x)))))

# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Извлекает текст второго элемента с классом "nowrap", находящегося внутри элемента с классом "form-group".
    x_element = webdriver.find_element(By.CSS_SELECTOR, "[class='form-group'] .nowrap:nth-child(2)").text
    # Текст передается в функцию calc, которая преобразует его в число, вычисляет результат и сохраняет его строковое представление в переменной y.
    y = calc(x_element)

    # Заполняет поле ввода текста на веб-странице, находя элемент <input /> с классом form-control внутри <div> с классом form-group, который является потомком <div> с классом container.
    input_area = webdriver.find_element(By.CSS_SELECTOR, 'div.container div.form-group input.form-control').send_keys(y)

    # Отмечает чекбокс на веб-странице, находя элемент <input /> с атрибутом type checkbox внутри элемента с классом form-check.
    checkbox = webdriver.find_element(By.CSS_SELECTOR, "div.form-check [type='checkbox']").click()

    # Выбирает радиокнопку на веб-странице, ищя элемент <input /> с атрибутами name, равным "ruler", и value, равным "robots".
    radio_button = webdriver.find_element(By.CSS_SELECTOR, "[name='ruler'][value='robots']").click()

    # Нажимает кнопку отправки формы, находя элемент <input /> с атрибутом type="submit", являющийся прямым потомком элемента <form>.
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "form > [type='submit']").click()

    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа

    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


except ValueError as e:
    print(f"Произошла ошибка при обработке значений на веб-странице: {e}")

# Код внутри блока finally будет выполнен в любом случае
finally:
    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Закрывает браузер
    webdriver.quit()