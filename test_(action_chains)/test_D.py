import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver import Keys # Импортируется класс Keys из модуля webdriver библиотеки Selenium, который содержит специальные клавиши, такие как ENTER, ESC и TAB, для имитации нажатий в автоматизированных тестах веб-приложений.
from selenium.webdriver.common.action_chains import ActionChains  # Импортирует класс ActionChains для выполнения сложных пользовательских действий (клик, перемещение мыши, перетаскивание).




# Ссылка на страницу
link = 'https://parsinger.ru/selenium/7/7.3.5/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке
    time.sleep(1)  # Убеждается что открыта искомая страница
    # Находит левый и правый контейнеры с интерактивными элементами на странице.
    left_container = driver.find_element(By.ID, "scrollable-container-left")
    right_container = driver.find_element(By.ID, "scrollable-container-right")

    # Переключается на левый контейнер и нажимает кнопку "END" переключаясь на каждый интерактвный элемент внутри контейнера.
    ActionChains(driver).click(left_container).send_keys(Keys.END).perform()
    # Переключается на правый контейнер и нажимает кнопку "END" переключаясь на каждый интерактвный элемент внутри контейнера.
    ActionChains(driver).click(right_container).send_keys(Keys.END).perform()
    # Убеждается, что все действия выполнены успешно.
    time.sleep(1)

    # Находит элемент с результатом по его ID и выводит его текст в качестве ответа
    print(f'Ответ: {driver.find_element(By.ID,'passwordContainer').text.split(":")[1].strip()}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")