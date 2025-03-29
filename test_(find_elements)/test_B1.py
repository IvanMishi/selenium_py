import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/3/3.3.3/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    total_digit = []


    # Каскадный поиск: находит родительский элемент и затем его дочерние элементы ввода (input) с помощью метода find_elements().
    # Находит родительский элемент.
    parent_element = webdriver.find_element(By.ID, 'linksContainer')
    # Проходит по каждому дочернему элемемену внутри родительского с тегом 'a' и вводит "Пользовательский текст".
    for child_element in parent_element.find_elements(By.TAG_NAME, "a"):
        stormtrooper_value = child_element.get_attribute('stormtrooper')  # Получаем значение атрибута
        if stormtrooper_value and stormtrooper_value.isdigit():  # Проверяем, содержит ли значение только числа
            total_digit.append(stormtrooper_value)

    check_area = webdriver.find_element(By.ID,'inputNumber').send_keys(sum(list(map(int, total_digit))))
    check_button = webdriver.find_element(By.ID, 'checkBtn').click()
    print(f'Ответ: {webdriver.find_element(By.ID,'feedbackMessage').text.split(":")[1].strip()}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`