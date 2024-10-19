import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import Select # Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.5/5/1.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Ищет родительские элементы с текстовыми полями "gray" и "blue", а также кнопкой "submit".
    parent_elements = webdriver.find_elements(By.CSS_SELECTOR, "[id='main-container'] > div")

    # Перебирает каждый найденный элемент в списке родительских элементов.
    for child_element in parent_elements:
        # Находит span внутри каждого родительского элемент и получает тест с цветом в формате hex
        span_element = child_element.find_element(By.CSS_SELECTOR, "[id='main-container'] > div > span").text

        # Находит select внутри каждого родительского элемент и выбирает опцию с значением цвета поученным из span
        select_element = Select(child_element.find_element(By.TAG_NAME, "select")).select_by_value(span_element)

        # Находит элемент кнопки, соответствующий цвету, и выполняет клик по нему.
        color_btn_element = child_element.find_element(By.CSS_SELECTOR,f"[id='main-container'] > div > div [data-hex='{span_element}']").click()
        # Находит checkbox и кликает по нему для отметки.
        checkbox_btn_element = child_element.find_element(By.CSS_SELECTOR,"[id='main-container'] > div > [type='checkbox']").click()
        # Находит текстовое поле и вводит в него значение цвета, полученное из span.
        input_text_element = child_element.find_element(By.CSS_SELECTOR,"[id='main-container'] > div > [type='text']").send_keys(span_element)
        # Находит кнопку подтверждения и кликает по ней.
        check_btn_element = child_element.find_element(By.CSS_SELECTOR, "[id='main-container'] > div > button").click()

    check_all_button = webdriver.find_element(By.CSS_SELECTOR, "body > button").click()

    time.sleep(1)
    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`