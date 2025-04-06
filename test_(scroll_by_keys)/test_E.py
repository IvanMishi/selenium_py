import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains  # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/7/7.3.5/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке
    time.sleep(1)  # Убеждается что открыта искомая страница

    left_container = driver.find_element(By.ID, "scrollable-container-left")
    ActionChains(driver).click(left_container).send_keys(Keys.END).perform()

    right_container = driver.find_element(By.ID, "scrollable-container-right")
    ActionChains(driver).click(right_container).send_keys(Keys.END).perform()
    time.sleep(1)

    #Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {driver.find_element(By.ID,'passwordContainer').text.split(":")[1].strip()}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")