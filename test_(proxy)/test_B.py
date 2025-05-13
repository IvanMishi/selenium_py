import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Определяет адрес прокси-сервера, который будет использоваться для интернет-соединения.
#proxy = '8.210.83.33:80'
# Cсылка на страницу
link = 'https://2ip.ru/'
# Создает объект ChromeOptions для настройки параметров браузера Chrome.
chrome_options = webdriver.ChromeOptions()
# Добавляет аргумент с прокси-сервером в настройки браузера.
#chrome_options.add_argument('--proxy-server=%s' % proxy)
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome(options=chrome_options) as driver:
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
