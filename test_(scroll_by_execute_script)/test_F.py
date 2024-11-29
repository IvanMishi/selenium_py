import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# ссылка на страницу
link = "https://parsinger.ru/selenium/5.7/1/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Инициализация переменной для хранения общего значения
total = 0

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    count = 0
    sum_of_numbers = 0  # Переменная для хранения суммы чисел
    count = 0
    parrent = webdriver.find_elements(By.CSS_SELECTOR, "[class='button-container']")

    for element in parrent:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        count += 1

    time.sleep(1)
    print(count)
    alert_text = webdriver.switch_to.alert.text
    print(alert_text)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
