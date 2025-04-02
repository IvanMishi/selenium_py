import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains  # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).

# Ссылка на страницу
link = 'https://parsinger.ru/selenium/7/7.3.3/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке
    time.sleep(1)  # Убеждается что открыта искомая страница



    # Выполняет операцию нажатия на перечисленные клавиши
    ActionChains(webdriver).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('T').perform()
    # Выполняет операцию отпускания нажатых клвиш
    ActionChains(webdriver).key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).key_up('T').perform()
    # Убеждается, что все действия выполнены успешно.
    time.sleep(3)

    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'passwordContainer').text.split(":")[1].strip()}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
