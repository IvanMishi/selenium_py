# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# ссылка на страницу 
link = "http://suninjuly.github.io/huge_form.html"

# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

    
# Проверка существования элементов: находит все элементы на странице, которые являются элементами ввода (input) c помощью метода find_elements(), если элементы найдены, заполняет данными.

    elements = browser.find_elements(By.TAG_NAME, "input")
    input_list = [] # cоздает пустой список для хранения найденных элементов
    for element in elements: # перебирает все найденные элементы
        input_list.append(element) # добавляет каждый найденный элемент в список input_list

# проверяет наличие найденных элементов 
    if elements: # если были найдены элементы
        for i in range(min(len(elements), len(input_list))): # Определяет количество элементов, которые нужно обработать (минимум из длин обоих списков)
            elements[i].send_keys("Мой ответ") # Заполняет текстовые поля элементов текстом "Мой ответ"


# находит и нажимает кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

# код внутри блока finally будет выполнен в любом случае
finally:
    # успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла