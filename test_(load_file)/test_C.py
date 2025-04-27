import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import os # Модуль  для работы с операционной системой, чтобы указать путь к файлу
import re # Модуль для работы с регулярными выражениями
from selenium.webdriver.chrome.service import Service


# Ссылка на страницу
link = "https://www.lambdatest.com/selenium-playground/download-file-demo"

# Измеряет время выполнения определенного участка кода.
start = time.time()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Оставляет браузер открытым после завершения скрипта.
g = Service()



with webdriver.Chrome(options=options, service=g) as driver:  # Создаёт экземпляр драйвера Chrome.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается, что открыта искомая страница.

    # Находит находит кнопку для укачивания файла.
    click_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
    # Нажимает на нее.
    click_button.click()
    time.sleep(3)    #Убеждается, что файл добавлен в директорию.

    # Указываем полный путь к директории куда будет скачиваться файл.

    path_upload = os.path.expanduser("~/Documents/GIT/selenium_py/test_(load_file)/")  # Используем os.path.expanduser для правильной обработки домашней директории.
    #file_path = os.path.join(path_upload, 'file.txt')
    load_file = driver.find_element(By.ID, "file")
    load_file.send_keys(path_upload)

    button_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Убеждается, что наш файл скачался в нужную директорию
    file_name = "LambdaTest.pdf"    #имя ожидаемого файла
    file_path = path_download + file_name    #путь до ожидаемого файла + имя файла
    assert os.access(file_path, os.F_OK) == True    #проведение проверки на наличие файла
​​​​​    print("Файл в скачался в указаную директорию")

    # Проверка на то ,что файл не пуст 
    files = glob.glob(os.path.join(path_download, "*.*"))

    for file in files:
        a = os.path.getsize(file)
        if a > 10:
            print("Файл не пуст")
        else:
            print("Файл пуст")

    # Удаление скаченного файла из директории
    files = glob.glob(os.path.join(path_download, "*.*"))
    # Данная конструкция, будет пробегать циклом по нужной нам директории и удалять все файлы в ней ,по очереди.
    for file in files:
        os.remove(file)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
