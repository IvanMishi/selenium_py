import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
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

    # Получает текущую дату и прибавляет к ней 10 дней, форматирует под условия сайта
    future_date_10 = (datetime.datetime.utcnow() + datetime.timedelta(days=10)).strftime("%m/%d/%Y")
    print(f'Сегдняшняя дата: {datetime.datetime.utcnow()}')
    print(f'Дата через 10 дней:{future_date_10}')


    print('Находит поле для выбора даты')
    date_area = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
    print('Удаляет текущую дату')
    [date_area.send_keys(Keys.BACKSPACE) for _ in range(10)]
    print('Визуально убеждается что текущая дата удалена')
    time.sleep(3)

    print('Устаеавливает  дату через 10 дней от текущей')
    date_area.send_keys(f'{future_date_10}')
    print('Визуально убеждается что текущая дата установлена')
    time.sleep(3)
