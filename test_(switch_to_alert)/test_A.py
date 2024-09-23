import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('http://parsinger.ru/blank/modal/1/index.html')
    webdriver.find_element(By.ID, 'alert').click()
    time.sleep(1)

    # Переключается на alert и выводит его текст
    alert = webdriver.switch_to.alert
    print(alert.text)

    time.sleep(1)
    # Закрывает alert кнопкой "OK"
    alert.accept()
    time.sleep(1)
