import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

# Cсылка на страницу
link = "https://parsinger.ru/selenium/3/3.2.4/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит кнопку на веб-странице и нажимает на нее
    find_button = webdriver.find_element('id', 'secret-key-button').click()
    # Вывводит значение атрибута в качестве ответа в консоль
    print(f'Ответ: {webdriver.find_element('id','secret-key-button').get_attribute('data')}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
