import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
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

    # Создание локатора ндля выбора даты на 10 дней вперед от текущей
    print('Определяет текущую дату')
    now_date = datetime.datetime.utcnow().strftime("%m,%d,%Y")
    print(f'Сегодняшняя дата {now_date.replace(",", "/")}')
    print('Устанавливает к текущей дате 10 дней')
    date_future = int(now_date.split(",")[1]) + 10
    print(f'Дата через десять дней: {date_future} число')
    print('Создает локатор для выбора элемента на 10 днй вперед от текущей даты')
    locator_new_date = f"//div[@aria-label='Choose Tuesday, May {date_future}th, 2025']"
    print(f'Синтаксис созданого локатора: {locator_new_date}')


    print('Находит поле для выбора даты')
    date_area = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
    print('Удаляет текущую дату')
    [date_area.send_keys(Keys.BACKSPACE) for _ in range(10)]
    print('Визуально убеждается что текущая дата удалена')
    time.sleep(3)
    print('Устаеавливает текущую дату повторно')
    date_area.send_keys(f'{now_date.replace("," , "/")}')
    print('Визуально убеждается что текущая дата установлена')
    time.sleep(3)

    print('Находит дату по локатору')
    date_last_10 = driver.find_element(By.XPATH, locator_new_date)
    print('Выбирает найденную дату')
    date_last_10.click()
    date_area.send_keys(Keys.RETURN)
    print('Визуально убеждается дата установлена успешно')
    time.sleep(5)

