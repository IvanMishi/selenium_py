import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import Select # Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу.
link = 'https://suninjuly.github.io/selects1.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.


    # Находит элементы с числами на веб странице и получает из них текст
    a_element = webdriver.find_element(By.CSS_SELECTOR, "[id='num1']").text
    b_element = webdriver.find_element(By.CSS_SELECTOR, "[id='num2']").text
    # Преобразует полученные значения в числовые и складывает их
    sum = (int(a_element) + int(b_element))

    # Находит выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    select_list = Select(webdriver.find_element(By.TAG_NAME, "select"))
    # Выбирает опции в выпадающем списке по значению равной сумме чисел
    select_list.select_by_value(str(sum))

    # Нажимает кнопку отправки формы на веб-странице.
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
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