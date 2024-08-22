import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.9/2/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Ожидает присутствия элемента с искомым ID и нажимает на него, если этот элемент видим пользователю
    if WebDriverWait(webdriver, 60).until(EC.presence_of_element_located((By.ID, "qQm9y1rk"))):
        element_is_presence = webdriver.find_element(By.ID, "qQm9y1rk")
        if WebDriverWait(webdriver, 60).until(EC.visibility_of(element_is_presence)):
            element_is_presence_and_visibility = element_is_presence
            element_is_presence_and_visibility.click()

    # Ожидает, что модальное окно появится, переключается на него и выводит текст в консоль
    print(f'Ответ:{WebDriverWait(webdriver, 60).until(EC.alert_is_present()).text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`
