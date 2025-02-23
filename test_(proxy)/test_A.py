import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Создает объект ChromeOptions для настройки параметров браузера Chrome.
options_chrome = webdriver.ChromeOptions()
# Добавляет расширение (в данном случае 'coordinates.crx') в браузер Chrome.
#options_chrome.add_extension('coordinates.crx')

# Cсылка на страницу
link = 'https://2ip.ru/'
with webdriver.Chrome(options=options_chrome) as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    # Ждет 1 секунду
    time.sleep(1)
    # Находит элемент по ID 'd_clip_button', затем находим вложенный элемент span, и выводим его текст в консоль.
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    # Ждет 1 секунду
    time.sleep(1)
