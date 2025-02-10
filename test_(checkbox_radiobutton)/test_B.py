import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'http://parsinger.ru/selenium/4/4.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.

    # Находит все элементы чекбокс на веб странице
    checkboxs = webdriver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")

    # Перебирает каждый найденный элемент в списке checkboxs
    for element in checkboxs:
        element.click() # Отмечает каждый найденый чекбокс

    # Нажимает кнопку отправки формы на веб-странице
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='button']").click()
    time.sleep(1)  # Визуально убеждается, что все действия выполнены.

    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'result').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

