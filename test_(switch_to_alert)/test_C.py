import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('http://parsinger.ru/blank/modal/1/index.html')
    # Нажимает на кнопку для вызова модального окна Confirm
    webdriver.find_element(By.ID, 'confirm').click()
    time.sleep(1)

    # Получает confirm на веб-странице и переключается на него
    confirm = webdriver.switch_to.alert
    time.sleep(1)
    # Выводит текст предупреждения (confirm) в консоль
    print(confirm.text)
    # Принимает и закрывает confirm путем нажатия кнопки "OK" (accept), заменить на .dismiss() чтобы нажать на кнопку "Отмена"
    confirm.accept()
    time.sleep(1)