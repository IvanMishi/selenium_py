import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import Select # Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'http://parsinger.ru/selenium/6/6.html '
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит элемент с числом на веб странице и получает его текст
    a_element = webdriver.find_element(By.CSS_SELECTOR, "[id='text_box']").text
    # Вычисляет выражение и преобразует полученные значения в строку, извлекае символы с 3 по 4 
    x = str((eval(a_element)))[2:4]

    # Находит выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    dropdown_element = Select(webdriver.find_element(By.TAG_NAME, "select"))
    # Выбирает опции в выпадающем списке по индексу

    dropdown_element.select_by_value("60")

    # Нажимает кнопку отправки формы на веб-странице.
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='button']").click()

    # Выводит значение переменной с id='result' в качестве ответа.
    print(f'Ответ:{webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`