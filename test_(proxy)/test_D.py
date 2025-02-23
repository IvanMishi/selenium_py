import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.chrome.service import Service  # Импортируем сервис для управления Chrome.
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем менеджер для автоматической установки ChromeDriver.

# Настраивает параметры прокси-сервера
options = {'proxy': {
    'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867", # Указывает HTTP прокси с аутентификацией
    'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867", # Указывает HTTP прокси с аутентификацией
    }}

# Cсылка на страницу
link = 'https://2ip.ru/'
with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) as driver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    # Находит элемент по ID 'd_clip_button', затем находим вложенный элемент span, и выводим его текст в консоль.
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    # Ждет 1 секунду
    time.sleep(1)