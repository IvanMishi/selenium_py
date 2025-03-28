import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

# Cсылка на страницу
link = "https://parsinger.ru/selenium/3/3.2.2/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная  содержит текст, с ожидаемым резултатом.
expected_result = "Thank you for submitting the form!"


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.


    # Находит поле для ввода текста на веб-странице
    textarea = webdriver.find_element("id", "codeInput").send_keys('Дрогон')
    pass_button = webdriver.find_element("id","clickButton").click()
    print(f'Ответ: {webdriver.find_element("id", "codeOutput").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
