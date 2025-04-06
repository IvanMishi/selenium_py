import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from selenium.common.exceptions import TimeoutException # Импортирует исключение для обработки тайм-аутов

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    while True:
        # Находит кнопку на веб-странице по классу 'search-link' и нажимаем на нее
        search_link_button = webdriver.find_element(By.CLASS_NAME, 'search-link').click()
        try:
            # Ожидает, пока подстрока "qLChv49" появится в текущем URL
            text_url = WebDriverWait(webdriver, 0.2).until(EC.url_contains("qLChv49"))
            # Если подстрока найдена, нажимает на кнопку для получения ответа
            webdriver.find_element(By.TAG_NAME, 'button').click()
            # Извлекаем текст ответа из элемента <p>, разделяет его по двоеточию и берет правую часть
            print(f'Ответ: {webdriver.find_element(By.TAG_NAME, 'p').text.split(":")[1].strip()}')
            # Если ответ получен, прогамма выполнена
            if text_url:
                break
        # Если произошло время ожидания, продолжает цикл, не делая ничего
        except TimeoutException:
            pass
# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")