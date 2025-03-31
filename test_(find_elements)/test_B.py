import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'http://suninjuly.github.io/huge_form.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Каскадный поиск: находит родительский элемент и затем его дочерние элементы ввода (input) с помощью метода find_elements().
    # Находит родительский элемент.
    parent_element = driver.find_element(By.CSS_SELECTOR, 'form[action="#"][method="get"]')

    # Проходит по каждому дочернему элемемену внутри родительского с тегом 'input' и вводит "Пользовательский текст".
    [child_element.send_keys("Пользовательский текст") for child_element in parent_element.find_elements(By.TAG_NAME, "input")]

    # Находит и нажимает кнопку Submit с помощью правил на основе CSS
    button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Получает alert на веб-странице
    alert = driver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
    # Убеждается, что все действия выполнены успешно.
    time.sleep(3)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
