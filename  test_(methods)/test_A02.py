import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

# Cсылка на страницу
link = "https://parsinger.ru/selenium/3/3.2.3/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная  содержит текст, с ожидаемым резултатом.
expected_result = "Thank you for submitting the form!"


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит кнопку на веб-странице и нажимает на нее
    show_button = webdriver.find_element("id","showTextBtn").click()
    #
    text_element = webdriver.find_element('id', 'text1').text
    # Находит поле для ввода текста на веб-странице и заполняет данными
    textarea = webdriver.find_element("id", "userInput").send_keys(text_element)
    # Находит кнопку кпроверки кода на веб-странице и нажимает на нее
    check_button = webdriver.find_element("id", "checkBtn").click()

    print(f'Ответ: {webdriver.find_element("id", "text2").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

# Cсылка на страницу
link = "https://parsinger.ru/selenium/3/3.2.3/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная  содержит текст, с ожидаемым резултатом.
expected_result = "Thank you for submitting the form!"


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит кнопку на веб-странице и нажимает на нее
    show_button = webdriver.find_element("id","showTextBtn").click()
    #
    text_element = webdriver.find_element('id', 'text1').text
    # Находит поле для ввода текста на веб-странице и заполняет данными
    textarea = webdriver.find_element("id", "userInput").send_keys(text_element)
    # Находит кнопку кпроверки кода на веб-странице и нажимает на нее
    check_button = webdriver.find_element("id", "checkBtn").click()

    print(f'Ответ: {webdriver.find_element("id", "text2").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
