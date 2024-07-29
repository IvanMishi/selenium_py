# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание экземпляра WebDriver с использованием браузера Chrome
with webdriver.Chrome() as webdriver:
    # Загрузка указанного URL в веб-браузере
    webdriver.get("https://parsinger.ru/selenium/5.7/4/index.html")
    
    # Прокрутка страницы до тех пор, пока на странице не будет как минимум 1000 элементов input
    while len(webdriver.find_elements(By.CSS_SELECTOR, "input")) < 1000:
        # Находим последний дочерний контейнер на странице
        last = webdriver.find_element(By.CSS_SELECTOR, ".child_container:last-child")
        # Прокручиваем последний дочерний элемент в видимую область
        webdriver.execute_script("return arguments[0].scrollIntoView(true)", last)
    
    # Перебираем все элементы чекбоксов на странице
    for checkbox in webdriver.find_elements(By.CSS_SELECTOR, "input"):
        # Проверяем, является ли значение чекбокса четным
        if int(checkbox.get_attribute("value")) % 2 == 0:
            # Прокручиваем чекбокс в видимую область
            webdriver.execute_script("return arguments[0].scrollIntoView(true)", checkbox)
            # Устанавливаем чекбокс в состояние выбранного
            checkbox.click()
    
    # Находим и нажимаем кнопку alert на странице
    webdriver.find_element(By.CSS_SELECTOR, ".alert_button").click()
    
    # Выводим текст из диалогового окна alert
    print(webdriver.switch_to.alert.text)