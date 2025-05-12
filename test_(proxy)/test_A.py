import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.alert import Alert


# Создает объект ChromeOptions для настройки параметров браузера Chrome.
options_chrome = webdriver.ChromeOptions()
# Добавляет расширение (в данном случае 'coordinates.crx') в браузер Chrome.
#options_chrome.add_extension('coordinates.crx')

# Ссылка на страницу
link = 'https://2ip.ru/'
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome() as driver:
    # Переходит по ссылке
    driver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Находит элемент по ID "d_clip_button", затем находим вложенный элемент span, и выводит его текст в консоль.')
    print(f'Ваш IP: {driver.find_element(By.ID, "d_clip_button").find_element(By.TAG_NAME, "span").text}')
    time.sleep(1)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
