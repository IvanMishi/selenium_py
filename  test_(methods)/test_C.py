import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/selenium/5.5/1/1.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит поля для ввода текста на веб-странице
    elements = webdriver.find_elements(By.TAG_NAME, "input")
    # Перебирает каждый найденный элемент в списке elements
    for element in elements:
        # Очищает текст в каждый элемент ввода
        element.clear()
    # Нажиамет кнопку для проверки резуьтата
    check_button = webdriver.find_element(By.CSS_SELECTOR, "[id='checkButton']").click()

    # Переключается на alert и выводит его текст в консоль.
    alert = webdriver.switch_to.alert
    print(alert.text)
    time.sleep(1)  # Визуально убеждается, что переключился на alert
    # Закрывает alert кнопкой "OK"
    alert.accept()
    time.sleep(1)  # Визуально убеждается, что alert закрылся

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
