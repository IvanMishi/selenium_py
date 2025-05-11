import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import datetime

# Cсылка на страницу
link = "https://parsinger.ru/selenium/6/6.2.1/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'


    print('Создает переменную содержащую настоящую время и дату в формате  Час-Минуты-Секунды - день - месяц - Год .')
    now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
    print('Имя уникального скриншота с датой и временем.')
    name_screenshot = "screenshot " + now_date + ".png"
    print(name_screenshot)
    print('Скриншот по найденному элементу  сохранен в директорию созданную в проекте в папке screen')
    driver.find_element(By.ID, "this_pic").screenshot('screen/' + name_screenshot)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
