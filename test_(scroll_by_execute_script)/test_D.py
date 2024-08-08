# Импортирует необходимые библиотеки
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# Измеряет время выполнения определенного участка кода.
start = time.time()
# Открывает браузер Chrome
with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get("https://parsinger.ru/selenium/5.7/4/index.html")
    # Убеждается что открыта искомая страница
    time.sleep(1)
    # Прокручивает страницу до тех пор, пока на странице не будет как минимум 1000 элементов input
    while len(webdriver.find_elements(By.CSS_SELECTOR, "input")) < 1000:
        # Находит последний дочерний контейнер на странице
        last = webdriver.find_element(By.CSS_SELECTOR, ".child_container:last-child")
        # Прокручивает последний дочерний элемент в видимую область
        webdriver.execute_script("return arguments[0].scrollIntoView(true)", last)

    # Перебираем все элементы чекбоксов на странице
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