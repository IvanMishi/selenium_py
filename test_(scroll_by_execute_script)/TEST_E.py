import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# ссылка на страницу
link = "http://parsinger.ru/scroll/4/index.html"

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Ищет все кнопки на странице
    buttons = webdriver.find_elements(By.CSS_SELECTOR, "[class='btn']")

    # Поиск внутри списка элементов: находит все элементы на странице, которые являются элементами содержащими текст c помощью метода find_elements()
    # Инициализация переменной для хранения общего значения
    total = 0

    # Перебирает каждый найденный элемент в списке buttons
    for element in buttons:
        # Прокручивает страницу до элемента, чтобы он был виден
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
        # Нажимает на элемент
        element.click()
        # Находит элемент с результатом после нажатия на каждую кнопку
        result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']")
        # Добавляет значение результата к общему значению
        total += int(result.text)
    # Выводит в консоль сумму всех резуьтатов найденых при нажатии на каждую кнопку
    print(total)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
