import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import os # Модуль  для работы с операционной системой, чтобы указать путь к файлу
import re # Модуль для работы с регулярными выражениями
from selenium.webdriver.chrome.service import Service


# Ссылка на страницу
link = "http://suninjuly.github.io/file_input.html"

# Измеряет время выполнения определенного участка кода.
start = time.time()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Оставляет браузер открытым после завершения скрипта.
g = Service()



with webdriver.Chrome(options=options, service=g) as driver:  # Создаёт экземпляр драйвера Chrome.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается, что открыта искомая страница.

    # Находит и заполняет поля
    input_first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Tester")
    input_last_name = driver.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Test")
    input_email = driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("test@test.ru")

    # Указываем полный путь к файлу
    # Предполагаем, что файл находится в папке "Documents"
    path_upload = os.path.expanduser("~/Documents/GIT/selenium_py/test_(load_file)/file.txt")  # Используем os.path.expanduser для правильной обработки домашней директории.
    #file_path = os.path.join(path_upload, 'file.txt')
    load_file = driver.find_element(By.ID, "file")
    load_file.send_keys(path_upload)

    button_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()


    # Получает путь к файлу и загружает его
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    load_file = driver.find_element(By.CSS_SELECTOR, "[name='file']")
    load_file.send_keys(file_path)
    button_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Получает alert на веб-странице
    alert = driver.switch_to.alert
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
