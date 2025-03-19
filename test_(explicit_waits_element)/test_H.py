import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.9/7/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница
    while True:
        # Находит все элементы 'input' и 'button' на странице
        check_list = [x for x in webdriver.find_elements(By.TAG_NAME, 'input')]
        button_list = [x for x in webdriver.find_elements(By.TAG_NAME, 'button')]

        for check, button in zip(check_list, button_list):
            try:
                # Проверяет, является ли чекбокс выбранным
                if WebDriverWait(webdriver, 10).until(EC.element_to_be_selected(check)):
                    button.click()
            # Если возникает ошибка, выводит сообщение с деталью ошибки
            except Exception as e:
                print(f'Произошла ошибка: {e}')
            # Проверяет не изменился ли  текст элемента с id 'result', если текст изменился - программа выполнена!
            if webdriver.find_element(By.ID, 'result').text != 'Проверьте все чекбоксы':
                print(webdriver.find_element(By.ID, 'result').text)
                break
        else:
            # Продолжит цикл, если не было выхода через break
            continue
        break

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
