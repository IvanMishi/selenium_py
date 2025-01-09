import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
 

# Cсылка на страницу
link = "https://parsinger.ru/selenium/5.5/4/1.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Инициализация переменной для хранения общего значения textarea
    total = 0
    # Инициализация переменной для хранения общего количества найденых  отмеченых чекбоксов
    numbers = 0


    # Ищет все родительские элементы на странице, содержащие текстовые поля gray и blue, а также кнопку submit
    parent_elements = webdriver.find_elements(By.CSS_SELECTOR, ".parent")

    # Перебирает каждый найденный элемент в списке родительских элементов
    for parent_element in parent_elements:
        # Находит gray внутри каждого родительского элемента
        gray_element = parent_element.find_element(By.CSS_SELECTOR, "[color='gray']").text
        # Находит blue внутри каждого родительского элемента
        blue_element = parent_element.find_element(By.CSS_SELECTOR, "[color='blue']").send_keys(gray_element)

        # Очищает поле gray внутри каждого родительского элемента
        gray_element = parent_element.find_element(By.CSS_SELECTOR, "[color='gray']").clear()
        # Находит кнопки 'submit' внутри каждого родительского элемента
        parent_button = parent_element.find_element(By.CSS_SELECTOR, "[class='parent'] > button").click()

    # Нажиамет кнопку для проверки резуьтата
    check_all_button = webdriver.find_element(By.ID, 'checkAll').click()
    # Получает текст у появившегося элемента с резуьтатом
    result = webdriver.find_element(By.ID, 'congrats').text
    # Выводит результат в консоль
    print(result)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
