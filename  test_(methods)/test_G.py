import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Cсылка на страницу
link = "https://parsinger.ru/selenium/6/6.2.1/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная  содержит текст, с ожидаемым резултатом.
expected_result = "Thank you for submitting the form!"


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    webdriver.find_element(By.ID, "this_pic").screenshot('file_name.png')



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
