# Импортирует необходимые библиотеки
# Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
from selenium.webdriver.support.ui import Select
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# Импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re

# Ссылка на страницу
link = "https://suninjuly.github.io/selects1.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
# Открывает браузер Chrome
with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)
    
    # Находит элементы с числами на веб странице и получает из них текст
    a_element = webdriver.find_element(By.CSS_SELECTOR, "[id='num1']").text
    b_element = webdriver.find_element(By.CSS_SELECTOR, "[id='num2']").text
    # Преобразует полученные значения в числовые и складывает их
    sum = (int(a_element)+int(b_element))

    # Находит выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    select_list = Select(webdriver.find_element(By.TAG_NAME, "select"))
    # Выбирает опции в выпадающем списке по значению равной сумме чисел
    select_list.select_by_value(str(sum))
  
    # Нажимает кнопку отправки формы на веб-странице
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

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

    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла
