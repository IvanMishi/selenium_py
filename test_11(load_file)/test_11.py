# Импортирует необходимые библиотеки
# Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
from selenium.webdriver.support.ui import Select
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# Импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re
# Импортирует модуль Python для работы с операционной системой, чтобы указать путь к файлу
import os


# Ссылка на страницу
link = "http://suninjuly.github.io/file_input.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
# Открывает браузер Chrome
with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Заполняет поля
    input_first_name = webdriver.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Tester")
    input_last_name = webdriver.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Test")
    input_email= webdriver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("test@test.ru")

    # Получает путь к файлу и загружает его
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    load_file = webdriver.find_element(By.CSS_SELECTOR, "[name='file']")
    load_file.send_keys(file_path)
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
