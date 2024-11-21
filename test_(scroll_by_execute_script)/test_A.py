import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import math # Модуль для выполнения математических расчетов
import re # Модуль для работы с регулярными выражениями



# Функция calc(x) возвращает результат логарифма натурального модуля выражения abs(12*math.sin(int(x)))
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Ссылка на страницу
link = "https://SunInJuly.github.io/execute_script.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит элемент с математическим выражением и сохраняет текст из этого элемента в переменную x
    x = webdriver.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    # Находит поле ввода на странице и вводит значение результата вычисления уравнения, используя функцию calc(x) для вычисления значения переменной x.
    input_area = webdriver.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(calc(x))
    # Нажимает кнопку отправки формы на веб-странице
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='submit']")
    

# Прокручивает страницу так, чтобы кнопка была видимой используя execute_script 
    webdriver.execute_script("return arguments[0].scrollIntoView(true);", button_submit)

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
# Браузер закрывается автоматически после завершения блока `with`