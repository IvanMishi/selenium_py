import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import re # Модуль для работы с регулярными выражениями


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
    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Закрывает браузер
    webdriver.quit()
