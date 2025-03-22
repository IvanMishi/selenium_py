import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.7.2/index.html'
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница

    # Находит и поле ввода и заполняет текстом
    find_area = webdriver.find_element(By.CLASS_NAME, 'search-box').send_keys('Test')
    # Находит и нажимает кнопку Поиск
    fungle_button = webdriver.find_element(By.ID,'search-button').click()

    WebDriverWait(webdriver, 10).until(EC.staleness_of(webdriver.find_element(By.ID,'old-result')))
    WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(webdriver.find_element(By.ID,'secret-button'))).click()  # Ожидание, пока кнопка станет доступна для клика
    print(f'Ответ: {webdriver.find_element(By.ID, 'result').text}')
    time.sleep(25)

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

