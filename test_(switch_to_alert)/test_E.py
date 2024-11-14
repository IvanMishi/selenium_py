import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.8/3/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    #Проверяет существование элементов: находит все элементы на странице, которые являются элементами типа чекбокс (checkbox) c помощью метода find_elements(), если элементы найдены, отмечает их.
    pin_codes = webdriver.find_elements(By.CSS_SELECTOR, ".pin")
    button_check = webdriver.find_element(By.CSS_SELECTOR, ".main #check")
    result = webdriver.find_element(By.CSS_SELECTOR, "#result")
    count = 0

    for pin in pin_codes:
        extracted_text = pin.text
        button_check.click()
        #time.sleep(1)
        alert = webdriver.switch_to.alert
        alert.send_keys(extracted_text)
        #time.sleep(2)
        alert.accept()
        #time.sleep(2)
        count+=1
        if result.text == 'Неверный пин-код':
           continue
        else:
            find = result.text
            break
print(f'Ответ: Элемент № {count} содержит верный пин-код {find}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`