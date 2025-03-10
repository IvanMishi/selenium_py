import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

with webdriver.Chrome() as browser: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    time.sleep(1) # Ждет 1 секунду
    # Используем JavaScript для открытия нескольких новых вкладок с указанными URL
    browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')  # Открывает первую вкладку
    browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')  # Открывает вторую вкладку
    browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')  # Открывает третью вкладку
    browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')  # Открывает четвертую вкладку
    browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')  # Открывает пятую вкладку
    browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')  # Открывает шестую вкладку

    # Перебирает все открытые вкладки браузера
    for x in range(len(browser.window_handles)):  # Получает количество открытых вкладок
        browser.switch_to.window(browser.window_handles[x])  # Переключаемся на текущую вкладку по индексу
        time.sleep(1)  # Делает паузу в 1 секунду, чтобы страница успела загрузиться
        # Получает и выводит заголовок страницы и дескриптор вкладки
        print(browser.execute_script("return document.title;"),
              browser.window_handles[x])  # Печатаем заголовок и дескриптор вкладки