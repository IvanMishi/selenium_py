import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('http://parsinger.ru/blank/modal/1/index.html')
    # Нажимает на кнопку для вызова модального окна Prompt
    webdriver.find_element(By.ID, 'prompt').click()
    time.sleep(1)

    # Получает prompt на веб-странице и переключается на него
    prompt = webdriver.switch_to.alert
    # Заполняет поле текстом
    prompt.send_keys('Пользовательский текст')
    time.sleep(1)
    # Выводит текст предупреждения (prompt) в консоль
    print(prompt.text)
    # Принимает и закрывает prompt путем нажатия кнопки "OK" (accept)
    prompt.accept()
    # Выводит текст из элеммента c id='result' в консоль
    print(webdriver.find_element(By.ID, 'result').text)
    time.sleep(1)