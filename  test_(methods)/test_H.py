import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from faker import Faker # Импортируем класс Faker из установленной библиотеки
import datetime # Модуль  для работы с датами и временем
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://demoqa.com/date-picker'
# Измеряет время выполнения
start = time.time()
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")

with webdriver.Chrome() as driver:
    # Переходит по ссылке
    driver.get(link)
    print('Ожидает загрузку страницы.')
    WebDriverWait(driver, 60).until(EC.url_to_be(link))
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Находит поле для выбора даты')
    date_area = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
    print('Удаляет текущую дату')
    [date_area.send_keys(Keys.BACKSPACE) for _ in range(10)]

    print('Определяет текущую дату')
    now_date = datetime.datetime.utcnow().strftime("%d")
    print(f'Сегодняшняя дата {now_date}')
    print('Устанавливает к текущей дате 10 дней')
    date_future = int(now_date) + 10
    print('Создает локатор для выбора элемента на 10 днй вперед от текущей даты')
    locator_new_date = f"//div[@aria-label='Choose Tuesday, May {date_future}th, 2025']"
    print(f'Синтаксис созданого локатора: {locator_new_date}')
    print('Находит дату по локатору')
    time.sleep(5)
    date_last_10 = driver.find_element(By.XPATH, locator_new_date)
    time.sleep(5)
    print('Выбирает найденную дату')
    date_last_10.click()
    print('Визуально убеждается что все действия выполнены успешно')
    time.sleep(10)

