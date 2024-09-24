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

    # Находит кнопку для вызова alert и нажимает на нее.
    webdriver.find_element(By.ID, 'alert').click()
    # Переключается на alert и выводит его текст в консоль.
    alert = webdriver.switch_to.alert
    print(alert.text)
    time.sleep(1) # Визуально убеждается, что переключился на alert
    # Закрывает alert кнопкой "OK"
    alert.accept()
    time.sleep(1) # Визуально убеждается, что alert закрылся


    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`








