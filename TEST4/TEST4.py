# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице


# ссылка на страницу 
link = "http://suninjuly.github.io/huge_form.html"

# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)
    
# Находит все элементы на странице, которые являются элементами ввода (input) c помощью метода find_elements()
    elements = browser.find_elements(By.TAG_NAME, "input")
# Перебирает каждый найденный элемент в списке elements
    for element in elements:
    # Вводит текст "Мой ответ" в каждый элемент ввода
        element.send_keys("Мой ответ")
        
# находит и нажимает кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

# код внутри блока finally будет выполнен в любом случае
finally:
    # успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла
