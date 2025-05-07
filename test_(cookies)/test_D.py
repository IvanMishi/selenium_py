import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.2/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.

    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'  # Ошибка будет выведена в консоль в случае если URL не совпадают

    # Удаляет все cookies текущей сессии браузера
    driver.delete_all_cookies()
    # Ожидает появление элемента для вывода текста из него в качестве ответа. 
    print(f'Ответ: {WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "password"))).text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
