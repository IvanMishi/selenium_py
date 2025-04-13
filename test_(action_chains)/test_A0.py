import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains  # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from selenium.webdriver.support.wait import WebDriverWait

# Ссылка на страницу
link = 'https://demoqa.com/buttons'
# # Измеряет время выполнения
# start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке

    # Ожидает смены ссылки на странице.
    url = WebDriverWait(driver, 60).until(
        EC.url_to_be(link))
    print(driver.current_url)

    # # Находит элемент для выполнения операций клика.
    double_click_button = driver.find_element(By.ID, "doubleClickBtn")

    # right_click_button = driver.find_element(By.ID,"rightClickBtn")
    # click_button = driver.find_element(By.CSS_SELECTOR, "[id = '#eSA9j']")

    # Выполняет операцию двойного клика по элементу
    ActionChains(driver).double_click(double_click_button).perform()
    time.sleep(1)  # Визуально убеждается, что элемент был кликнут
    if driver.find_element(By.ID,'doubleClickMessage').text == 'You have done a double click':
        print('Двоиной клик выполнен успешно')

    # Выполняет операцию правого клика по элементу
    # ActionChains(driver).context_click(right_click_button).perform()
    # time.sleep(1)  # Визуально убеждается, что элемент был кликнут

    # Выполняет операцию клика по элементу
    #ActionChains(driver).click(click_button).perform()
    # time.sleep(1)  # Визуально убеждается, что элемент был кликнут


# # Завершение отсчета времени
# end = time.time()
# print(f"Время выполнения: {end - start} секунд.")