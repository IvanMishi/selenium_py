import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.3/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Добавляет куки в текущую сессию браузера')
    driver.add_cookie({"name": "secretKey", "value": "selenium123"})
    print('Обновляет страницу, чтобы изменения куки вступили в силу')
    driver.refresh()  
    print('Выводит текст из ожидаемого эемента с id = "password" в качестве ответа')
    print(f'Ответ:{WebDriverWait(webdriver, 60).until(EC.presence_of_element_located((By.ID, "password"))).text.split(":")[1].strip()}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")