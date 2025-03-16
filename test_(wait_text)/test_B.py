import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.6.2/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    ask_button = webdriver.find_element(By.ID, 'ask-jaskier').click()

    # Ожидает  элемент с искомым ID и нажимает, если элемент присутствует на странице
    element = WebDriverWait(webdriver, 60).until(EC.text_to_be_present_in_element_value((By.ID, 'recipe_field'), 'Селениумий'))


    # Ожидает, что модальное окно появится, переключается на него и выводит текст в консоль
    time.sleep(3)
    print(f'Ответ: {WebDriverWait(webdriver,10).until(EC.visibility_of_element_located((By.ID, 'password'))).text}')


    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Браузер закрывается автоматически после завершения блока `with`
