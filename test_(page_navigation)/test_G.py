import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

with webdriver.Chrome() as browser:
    browser.get("https://google.com") # Перейти на сайт Google

    # Четыре вкладки открываются последовательно, и на каждой из них загружается отдельный URL с помощью ещё одного вызова get().
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/1.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/2.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/3.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/4.html")
    time.sleep(2)
    # Цикл, в котором скрипт итерируется по всем открытым окнам браузера
    for x in range(len(browser.window_handles)):  # reversed(range(len(browser.window_handles))) Для итерирования  от последней вкладки к первой
        browser.switch_to.window(browser.window_handles[x]) # Переключение между вкладками
        # Вложенный цикл для обработки чекбоксовдля каждого сайта 
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()
        time.sleep(1)