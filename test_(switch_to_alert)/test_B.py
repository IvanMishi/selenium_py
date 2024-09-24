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

    # Находит кнопку для вызова Prompt и нажимает на нее.
    webdriver.find_element(By.ID, 'prompt').click()
    # Переключается на Prompt.
    prompt = webdriver.switch_to.alert
    time.sleep(1)  # Визуально убеждается, что переключился на Prompt.
    # Заполняет поле текстом.
    prompt.send_keys('Пользовательский текст')
    # Выводит текст предупреждения Prompt в консоль.
    print(prompt.text)
    # Закрывает Prompt кнопкой "OK"
    prompt.accept()
    time.sleep(1) # Визуально убеждается, что Prompt закрылся
    # Находит элемент с ID 'result', который содержит текст, введенный пользователем в prompt, и выводит его в консоль.
    print(webdriver.find_element(By.ID, 'result').text)

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`








