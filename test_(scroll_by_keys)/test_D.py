import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium_scripts.browser_setup import browser, random_generator


# Cсылка на страницу
link = "https://parsinger.ru/selenium/7/7.2/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    while True:  # Начинаем бесконечный цикл

        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = [x for x in webdriver.find_elements(By.CLASS_NAME, 'interactive')]
        # Обходим каждый элемент input в списке
        if not input_tags:
            break
        input_tags[0].send_keys(random_generator.word(), Keys.ENTER, Keys.DOWN)

    print(webdriver.find_element(By.ID, "hidden-password").text)
    time.sleep(25)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`