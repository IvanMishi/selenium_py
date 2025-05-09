import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/selenium/3/3.2.4/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Находит кнопку на веб-странице и нажимает на нее.')
    find_button = driver.find_element(By.ID, 'secret-key-button').click()
    print('Вывводит значение атрибута в качестве ответа в консоль')
    print(f'Ответ: {driver.find_element(By.ID,"secret-key-button").get_attribute("data")}')



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
