import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from selenium.webdriver.support.ui import Select

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/9/9.7.1/index.html'
# Измеряет время выполнения
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница

    adress_area = webdriver.find_element(By.ID, 'address').send_keys('Moscow')
    # Находит выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    select_list = Select(webdriver.find_element(By.ID, "payment"))
    # Выбирает из выпадающего списка по артибуту оплата картой
    select_list.select_by_value('card')
    # Находит и нажимает кнопку отправки формы
    submit_order_button = webdriver.find_element(By.ID, 'submit-order').click()


    #spinner_element =
    WebDriverWait(webdriver, 20).until(EC.invisibility_of_element(webdriver.find_element(By.ID,'spinner')))
    WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(webdriver.find_element(By.ID,'confirm-address'))).click()  # Ожидание, пока кнопка станет доступна для клика
    WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(webdriver.find_element(By.ID, 'get-code'))).click()  # Ожидание, пока кнопка станет доступна для клика

    print(f'Ответ: {webdriver.find_element(By.ID, 'result').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

