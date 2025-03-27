import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Cсылка на страницу
link = "https://parsinger.ru/selenium/6/6.2/index.html "
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная  содержит текст, с ожидаемым резултатом.
expected_result = "Thank you for submitting the form!"


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    next_page2_button = webdriver.find_element(By.CSS_SELECTOR, 'div a').click()
    next_page3_button = webdriver.find_element(By.CSS_SELECTOR, 'p a').click()
    webdriver.back()
    webdriver.back()


    # Находит кнопку для вызова alert и нажимает на нее.
    webdriver.find_element(By.ID, 'getPasswordBtn').click()
    # Переключается на alert и выводит его текст в консоль.
    alert = webdriver.switch_to.alert
    print(f'Ответ: {alert.text.split(":")[1].strip()}')
    time.sleep(1)  # Визуально убеждается, что переключился на alert
    # Закрывает alert кнопкой "OK"
    alert.accept()
    time.sleep(1)  # Визуально убеждается, что alert закрылся


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
