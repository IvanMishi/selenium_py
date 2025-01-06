# Операция "Цветовая Синхронизация"

# Откройте веб-сайт с помощью Selenium. Проанализируйте поля, с которыми предстоит работать.
# На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.
# Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.
# Секретный код появится только в том случае, если все поля успешно стали зелёными. Секретный код нужно будет вставить в поле для ответа на степик.


# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# ссылка на страницу 
link = "https://parsinger.ru/selenium/5.5/4/1.html"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

    # Инициализация переменной для хранения общего значения textarea
    total = 0
    # Инициализация переменной для хранения общего количества найденых  отмеченых чекбоксов
    numbers = 0



    # Ищет все родительские элементы на странице, содержащие текстовые поля gray и blue, а также кнопку submit
    parent_elements = browser.find_elements(By.CSS_SELECTOR, ".parent")



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
    checkAll_button = browser.find_element(By.ID, 'checkAll').click()
    # Получает текст у появившегося элемента с резуьтатом
    result = browser.find_element(By.ID, 'congrats').text
    # выводит результат в консоль
    print(result)



# оставляет пустую строку в конце файла
