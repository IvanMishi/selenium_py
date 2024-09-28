Откройте веб-сайт с помощью Selenium.
Активация Чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
Открывание Секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
Доступ к Секретным Данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.



# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# ссылка на страницу 
link = "http://parsinger.ru/selenium/4/4.html"

# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)
    
# Поиск внутри списка элементов: находит все элементы на странице, которые являются элементами содержащими текст c помощью метода find_elements()
    checkboxs = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")


    # Перебирает каждый найденный элемент в списке checkboxs
    for element in checkboxs:
        element.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='button']").click()
    time.sleep(1)
    result = browser.find_element(By.CSS_SELECTOR, "[id='result']").text

# код внутри блока finally будет выполнен в любом случае
finally:
    # успевает скопировать код за 3 секунд
    time.sleep(3)
    # закрывает браузер
    browser.quit()
    #Выводит результат суммирования данных из искомых элементов
    print("Ответ найден:", result)

# оставляет пустую строку в конце файла
