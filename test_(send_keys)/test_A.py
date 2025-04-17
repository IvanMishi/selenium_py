# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re
from faker import Faker # Импортируем класс Faker из установленной библиотеки




# Ссылка на страницу
link = "http://suninjuly.github.io/simple_form_find_task.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
fake = Faker("ru_Ru") # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)

# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Находит и заполняет поле First name фейковыми  данными
    input_first_name = webdriver.find_element(By.TAG_NAME, "input").send_keys(fake.first_name())
    # Находит и заполняет поле Last name фейковыми  данными
    input_last_name = webdriver.find_element(By.NAME, "last_name").send_keys(fake.last_name())
    # Находит и заполняет поле City фейковыми  данными
    input_сity = webdriver.find_element(By.CLASS_NAME, "form-control.city").send_keys(fake.city())
    # Находит и заполняет поле Country фейковыми  данными
    input_сountry = webdriver.find_element(By.ID, "country").send_keys(fake.country())
    # Находит и нажимает кнопку Submit
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "button.btn").click()
    # Убеждается, что все данные заполнены успешно.
    time.sleep(10)

    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# Код внутри блока finally будет выполнен в любом случае
finally:
    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Закрывает браузер
    webdriver.quit()
