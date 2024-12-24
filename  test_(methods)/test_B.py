import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver import Keys  # Импортируется класс Keys из модуля webdriver библиотеки Selenium, который содержит специальные клавиши, такие как ENTER, ESC и TAB, для имитации нажатий в автоматизированных тестах веб-приложений.


# ссылка на страницу
link = "https://parsinger.ru/selenium/5.5/2/1.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    list_input = []  # Инициализирут пустой список для хранения обработанных элементов ввода
    sum_of_numbers = 0  # Переменная для хранения суммы чисел

    # Ищет все элементы ввода (input) на странице с использованием метода find_elements
    input_elements = webdriver.find_elements(By.TAG_NAME, "input")

    # Перебирает каждый найденный элемент input
    for element in input_elements:
        # Проверяет, не отключен ли элемент с помощью атрибута 'disabled'
        if not element.get_attribute('disabled'):
            # Если элемент не отключен, очищает его содержимое
            element.clear()


    # Перебирает каждый найденный элемент input
    for element in input_elements:
        # Проверяет, включен ли элемент, используя метод .is_enabled()
        if element.is_enabled():
            # Если у элемента нет атрибута 'disabled', то очищаем его содержимое
            #        if not element.get_attribute('disabled'):

            # то очищаем его содержимое
            element.clear()
    # Находит кнопку с идентификатором 'checkButton' и кликаем по ней
    button_check = webdriver.find_element(By.CSS_SELECTOR, "[id='checkButton']").click()
    
    # получает alert на веб-странице
    alert = browser.switch_to.alert
    # сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # ждет 2 секунды
    time.sleep(2)
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
    print('Ответ', actual_result)
    # браузер закроется автоматически после завершения блока `with`

# оставляет пустую строку в конце файла


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`