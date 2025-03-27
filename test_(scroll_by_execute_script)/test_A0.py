import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями



# Ссылка на страницу
link = "https://parsinger.ru/selenium/6/6.5/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.



    # Прокручивает страницу так, чтобы кнопка была видимой используя execute_script
    webdriver.execute_script("return arguments[0].scrollIntoView(true);", webdriver.find_element(By.ID,'target'))
    button = webdriver.find_element(By.ID,'target').click()
    print( f'Ответ: {WebDriverWait(webdriver, 60).until(EC.visibility_of_element_located((By.ID, 'secret-key'))).text.split(":")[1].strip()}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")