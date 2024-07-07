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


# Ссылка на страницу
link = "http://suninjuly.github.io/find_xpath_form"
# Измеряет время выполнения определенного участка кода.
start = time.time()

# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Находит и заполняет поле "First name" с помощью правил на основе X-path
    input_first_name = webdriver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Ivan")
    # Находит и заполняет поле "Last name" с помощью правил на основе X-path
    input_last_name = webdriver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Petrov")
    # Находит и заполняет поле "City" с помощью правил на основе X-path
    input_city = webdriver.find_element(By.XPATH, "//input[@class='form-control city']").send_keys("Smolensk")
    # Находит и заполняет поле "Country" с помощью правил на основе X-path
    input_county = webdriver.find_element(By.XPATH, "//input[@id='country']").send_keys("Russia") 

    # Находит и нажимает кнопку Submit с помощью правил на основе X-path
    button_submit = webdriver.find_element(By.XPATH, "//button[@type='submit']").click()

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
    # Измеряет время выполнения кода и выводит его в консоль.
    print(f'Time is running {time.time() - start}')
    # Закрывает браузер
    webdriver.quit()

# Не забывает оставить пустую строку в конце файла
