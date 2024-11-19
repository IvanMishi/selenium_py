import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.7/4/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.


    # Прокручивает страницу до тех пор, пока на ней не появляется как минимум 1000 элементов типа input.
    while len(webdriver.find_elements(By.CSS_SELECTOR, "input")) < 1000:
        # Находит последний дочерний контейнер на странице
        last = webdriver.find_element(By.CSS_SELECTOR, ".child_container:last-child")
        # Прокручивает последний дочерний элемент в видимую область
        webdriver.execute_script("return arguments[0].scrollIntoView(true)", last)

    # Перебирает все элементы чекбоксов на странице.
    for checkbox in webdriver.find_elements(By.CSS_SELECTOR, "input"):
        # Проверяет, является ли значение чекбокса четным
        if int(checkbox.get_attribute("value")) % 2 == 0:
            # Прокручивает чекбокс в видимую область
            webdriver.execute_script("return arguments[0].scrollIntoView(true)", checkbox)
            # Выбирает чекбокс
            checkbox.click()

    # Находит и нажимает кнопку alert на странице
    webdriver.find_element(By.CSS_SELECTOR, ".alert_button").click()
    # Выводит текст из диалогового окна alert в качестве ответа
    print(f'Ответ: {webdriver.switch_to.alert.text}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`