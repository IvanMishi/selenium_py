import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/8/8.4.2/index.html'

# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}' # Ошибка будет выведена в консоль в случае если URL не совпадают

    for i in range(1, 5):
        iframe = driver.find_element(By.ID, f'frame{i}')
        driver.switch_to.frame(iframe)
        if i < 4:
            driver.find_element(By.CLASS_NAME, 'unlock-button').click()
            time.sleep(2)
        else:
            print(f' Ответ: {driver.find_element(By.TAG_NAME, 'h2').text}')
        driver.switch_to.default_content()

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
