import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.3.2/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(3)  # Убеждается что открыта искомая страница.

    webdriver.delete_all_cookies()  # Удаляет все файлы cookie в рамках текущего сеанса
    time.sleep(3)
    print(f'Ответ: {WebDriverWait(webdriver, 60).until(EC.visibility_of_element_located((By.ID, 'password'))).text.split(":")[1].strip()}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")