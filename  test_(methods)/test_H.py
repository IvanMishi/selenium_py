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

    # Создание локатора для выбора даты на 10 дней вперед от текущей
    print('Определяет текущую дату и прибаляет к ней 10 дней')
    future_date = datetime.datetime.utcnow() + datetime.timedelta(days=10)
    print(f'Через 10 дней будет {future_date}')


    print('Создает локатор для выбора элемента на 10 дней вперед от текущей даты')
    print('Форматирует дату')
    month = future_date.strftime("%B")  # Полное название месяца
    year = future_date.strftime("%Y")  # Получает полный год.
    day = future_date.strftime("%d").lstrip("0") # Получает день из объекта future_date, убирая ведущий ноль, чтобы получить только числовое значение.
    # Определяет суффикс для дня, основываясь на его значении (1st, 2nd, 3rd, th).
    # Если день в диапазоне от 4 до 20, используется суффикс "th". В противном случае, проверяются последние цифры для присвоения соответствующего суффикса.
    day_suffix = "th" if 4 <= int(day) <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(int(day[-1]), "th")
    formatted_day = f"{day}{day_suffix}" # Формирует строку для отображения дня с соответствующим суффиксом.
    weekday = future_date.strftime("%A")  # Получает день недели.
    # Формирует локатор для элемента на вебстранице, используя данные о дате и времени.
    # Локатор предназначен для выбора виджета даты, основанного на дне недели, месяце, особом формате дня с суффиксом и годе.
    locator_new_date = f"//div[@aria-label='Choose {weekday}, {month} {day}{day_suffix}, {year}']"
    print(f'Синтаксис созданного локатора: {locator_new_date}')  # Выводит сформированный локатор в консоль для проверки.


    print('Находит поле для выбора даты')
    date_area = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
    print('Удаляет текущую дату')
    [date_area.send_keys(Keys.BACKSPACE) for _ in range(10)]
    print('Визуально убеждается что текущая дата удалена')
    time.sleep(3)
    print('Устаеавливает текущую дату повторно')
    date_area.send_keys(f'{datetime.datetime.utcnow().strftime("%m/%d/%Y")}')
    print('Визуально убеждается что текущая дата установлена')
    time.sleep(3)

    print('Находит дату по локатору')
    date_last_10 = driver.find_element(By.XPATH, locator_new_date)
    print('Выбирает найденную дату')
    date_last_10.click()
    date_area.send_keys(Keys.RETURN)
    print('Визуально убеждается дата установлена успешно')
    time.sleep(5)
