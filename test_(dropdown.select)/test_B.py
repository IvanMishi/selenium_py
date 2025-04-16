import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import Select # Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/6/6.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}' # Ошибка будет выведена в консоль в случае если URL не совпадают


    # Находит элемент с числом на веб странице и получает его текст
    a_element = driver.find_element(By.CSS_SELECTOR, "[id='text_box']").text
    # Вычисляет выражение и преобразует полученные значения в строку.
    x = str((eval(a_element)))

    # Находит выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    dropdown_element = Select(driver.find_element(By.TAG_NAME, "select"))

    # Выбираем элемент по видимому тексту
    dropdown_element.select_by_visible_text(x)

    # Нажимает кнопку отправки формы на веб-странице.
    button_submit = driver.find_element(By.CSS_SELECTOR, "[type='button']").click()

    # Выводит значение переменной с id='result' в качестве ответа.
    print(f'Ответ: {driver.find_element(By.CSS_SELECTOR, "[id='result']").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
