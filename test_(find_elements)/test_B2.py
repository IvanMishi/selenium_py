import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/3/3.3.1/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}' # Ошибка будет выведена в консоль в случае если URL не совпадают
    total_digit = []

    parent_element = driver.find_element(By.ID, 'parent_id')
    for child_element in parent_element.find_elements(By.CLASS_NAME, "child_class"):
        child_element.click()
    print(f'Ответ: {child_element.get_attribute('password')}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`