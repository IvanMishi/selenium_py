import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import re # Модуль для работы с регулярными выражениями
import math

# Ссылка на страницу
link = "https://suninjuly.github.io/math.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

# Функция рассчитывает натуральный логарифм модуля произведения 12 и синуса целочисленного значения x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'


    print('Извлекает текст второго элемента с классом "nowrap", находящегося внутри элемента с классом "form-group".')
    x_element = driver.find_element(By.CSS_SELECTOR, "[class='form-group'] .nowrap:nth-child(2)").text
    print('Функция calc преобразует текст в число, вычисляет результат и сохраняет его строковое представление в переменной y.')
    y = calc(x_element)
    print('Заполняет текстовое поле <input /> с классом form-control, найденное внутри <div> с классом form-group, который находится в <div> с классом container.')
    input_area = driver.find_element(By.CSS_SELECTOR, 'div.container div.form-group input.form-control').send_keys(y)
    print('Отмечает чекбокс на веб-странице, находя элемент <input /> с атрибутом type checkbox внутри элемента с классом form-check.')
    checkbox = driver.find_element(By.CSS_SELECTOR, "div.form-check [type='checkbox']").click()
    print('Выбирает радиокнопку на веб-странице, ищя элемент <input /> с атрибутами name, равным "ruler", и value, равным "robots".')
    radio_button = driver.find_element(By.CSS_SELECTOR, "[name='ruler'][value='robots']").click()
    print('Нажимает кнопку отправки формы, находя элемент <input /> с атрибутом type="submit", являющийся прямым потомком элемента <form>.')
    button_submit = driver.find_element(By.CSS_SELECTOR, "form > [type='submit']").click()

    print('Получает alert на веб-странице')
    alert = driver.switch_to.alert
    print('Сохраняет текст предупреждения (alert) в переменной actual_result')
    actual_result = alert.text
    print('Выводит числовое значение полученного текста из alert в консоль в качестве ответа')
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
