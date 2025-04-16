import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/8/8.4.3/index.html'

# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}' # Ошибка будет выведена в консоль в случае если URL не совпадают


    for i in range(4):
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)
        driver.find_element(By.CLASS_NAME, 'button').click()
        time.sleep(1)

    print(f'Ответ: {driver.find_element(By.CLASS_NAME, 'password-container').text}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
