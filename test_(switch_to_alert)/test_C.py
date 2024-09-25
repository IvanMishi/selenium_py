import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'http://parsinger.ru/blank/modal/1/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.

    # Находит кнопку для вызова Confirm и нажимает на нее.
    webdriver.find_element(By.ID, 'confirm').click()
    # Переключается на Confirm.
    confirm = webdriver.switch_to.alert
    time.sleep(1)  # Визуально убеждается, что переключился на Confirm.
    # Выводит текст предупреждения Confirm в консоль.
    print(confirm.text)
    # Закрывает Confirm кнопкой "OK"
    confirm.accept()
    time.sleep(1) # Визуально убеждается, что Confirm закрылся

    
    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`








