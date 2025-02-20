import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By

# Настраивает параметры прокси-сервера
options = {'proxy': {
    'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867", # Указывает HTTP прокси с аутентификацией
    'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867", # Указывает HTTP прокси с аутентификацией
    }}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as webdriver:
    webdriver.get(url)
    # Ищем элемент на странице по ID 'd_clip_button', затем находим вложенный элемент по тегу 'span'
    # Получаем текст вложенного элемента и выводим его на экран
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)