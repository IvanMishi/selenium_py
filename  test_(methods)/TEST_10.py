# Откройте указанную веб-страницу с помощью Selenium. 
# На странице расположены 100 текстовых полей с текстом. Ваша задача — пройтись по каждому и удалить его содержимое. Причём быстро, у вас всего 5 секунд!
# После того как все поля будут очищены, нажмите на кнопку на странице.
# Скопируйте число, которое появится во всплывающем alert-окне, с помощью Selenium.
# Вставьте полученное число в поле ответа степик.

# считает кол-во инпутов





# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 




# ссылка на страницу 
link = "https://parsinger.ru/selenium/5.5/1/1.html"




# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)


    elements = browser.find_elements(By.TAG_NAME, "input")

# Перебирает каждый найденный элемент в списке elements
    for element in elements:
    # Чистит текст в каждый элемент ввода
        element.clear()


    button1 = browser.find_element(By.CSS_SELECTOR, "[id='checkButton']").click()

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

