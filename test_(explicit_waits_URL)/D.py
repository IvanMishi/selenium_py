import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from selenium.common.exceptions import TimeoutException # Импортирует исключение для обработки тайм-аутов
import re
# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.4.2/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница
    sum_numbers = []


# Находит элемент на веб-странице с текстом ссылки, содержащим подстроку 'Правильный путь', и нажимает на него.
    start_button = webdriver.find_element(By.ID, 'startButton').click()
    while True:
        try:
            # Ожидаем, что URL будет соответствовать заданному паттерну
            #if WebDriverWait(webdriver, 1).until(
                    EC.url_matches(r"^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$")):
                # Получаем текст элемента с классом ‘number’
            number = webdriver.find_element(By.CLASS_NAME, 'number').text
            print(number, )

                #sum_numbers.append(int(number))

                # Ожидаем, что URL будет равен указанному значению
                if WebDriverWait(webdriver, 10).until(
                        EC.url_to_be("https://parsinger.ru/selenium/9/9.4.2/index_2.html")):
                    # Здесь можно выполнять дополнительные действия после перехода на этот URL
                    print("Переход на index_2.html завершен.")

        except TimeoutException:
            # Если произошла ошибка тайм-аута, продолжаем цикл, ничего не делает
            pass

        print(sum(sum_numbers))
    time.sleep(252)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")