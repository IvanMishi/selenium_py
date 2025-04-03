import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains  # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/7/7.3.4/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке
    time.sleep(1)  # Убеждается что открыта искомая страница

    # Находит элемент для выполнения операции двойного клика.
    context_click_element = webdriver.find_element(By.ID, "context-area")
    click_element = webdriver.find_element(By.CSS_SELECTOR,'[data-action="get_password"]')

    # Выполняет операцию двойного клика по элементу
    ActionChains(webdriver).context_click(context_click_element).click(click_element).perform()
    time.sleep(1)  # Визуально убеждается, что элемент был кликнут

    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.CSS_SELECTOR, '[key="access_code"]').text}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
