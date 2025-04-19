import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import os # Модуль  для работы с операционной системой, чтобы указать путь к файлу
import re # Модуль для работы с регулярными выражениями
from selenium.webdriver.chrome.service import Service


# Ссылка на страницу
link = "https://www.lambdatest.com/selenium-playground/upload-file-demo"

# Измеряет время выполнения определенного участка кода.
start = time.time()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Оставляет браузер открытым после завершения скрипта.
g = Service()

# Указываем полный путь к файлу
# Предполагаем, что файл находится в папке "Documents"
path_upload = os.path.expanduser("~/Documents/GIT/file.txt")  # Используем os.path.expanduser для правильной обработки домашней директории.

with webdriver.Chrome(options=options, service=g) as driver:  # Создаёт экземпляр драйвера Chrome.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается, что открыта искомая страница.

    # Находит и заполняет поля
    click_button = driver.find_element(By.XPATH, "//input[@id='file']")
    click_button.send_keys(path_upload)  # Отправляет путь к файлу для загрузк

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
