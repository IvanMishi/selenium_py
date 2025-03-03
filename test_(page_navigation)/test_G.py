import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


with webdriver.Chrome() as browser:
    browser.get("https://stepik.org/course/104774/promo") # Вместо вкладки data; будет вкладка в которой будет загружен степик
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/1.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/2.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/3.html")
    browser.switch_to.new_window("tab")
    browser.get("http://parsinger.ru/blank/2/4.html")
    time.sleep(2)
    for x in range(len(browser.window_handles)):  # reversed(range(len(browser.window_handles))) Для итерирования
        browser.switch_to.window(browser.window_handles[x]) # от последней вкладки к первой
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()
        time.sleep(1)