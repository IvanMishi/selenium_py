import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Cсылка на страницу
link = "http://parsinger.ru/selenium/3/3.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Ищет все div с классом 'text'
    list_div = webdriver.find_elements(By.XPATH, "//div[@class='text']")
    # Перебирает  каждый div
    for i, div in enumerate(list_div):
        # Получает первый и третий теги <p> внутри каждого div
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')

        # Выводит их текст в конслоь
        print(f"Для div №{i + 1}, первый тег <p>: {first_p.text}, третий тег <p> : {third_p.text}")


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
