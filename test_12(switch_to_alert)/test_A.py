import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('http://parsinger.ru/blank/modal/1/index.html')
    webdriver.find_element(By.ID, 'alert').click()
    time.sleep(1)

    # Получает alert на веб-странице и переключается на него
    alert = webdriver.switch_to.alert
    # Выводит выводит содержимое title этого окна в консоль
    print(alert.text)
    time.sleep(1)
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
    time.sleep(1)
