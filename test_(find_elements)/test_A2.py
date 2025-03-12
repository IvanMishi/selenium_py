import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/3/3.3.2/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Поиск внутри списка элементов: находит все элементы с классом 'block' на странице с помощью метода find_elements().
    block_elements = webdriver.find_elements(By.CLASS_NAME, "block")
    # Пребирает каждый найденный элемент в списке block_elements
    for element in block_elements:
        # Находит кнопки в каждом блоке
        btn = element.find_element(By.CLASS_NAME, 'button')
        btn.click()

        # Выводит код в консоль
    print(webdriver.find_element(By.TAG_NAME, "password").text)



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
