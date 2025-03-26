import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.3/index.html'
# Измеряет время выполнения.
start = time.time()



with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Добавляет куки в текущую сессию браузера
    webdriver.add_cookie({"name": "secretKey", "value": "selenium123"}) 
    webdriver.refresh() # Обновляет страницу, чтобы изменения куки вступили в силу
    # Выводит текст из ожидаемого эемента с id = "password" в качестве ответа
    print(f'Ответ:{WebDriverWait(webdriver, 60).until(EC.presence_of_element_located((By.ID, "password"))).text.split(":")[1].strip()}')



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
