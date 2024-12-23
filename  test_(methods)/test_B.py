# Используя Selenium, откройте заданный веб-сайт. Убедитесь, что ваша машина готова к операции.
# : У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те, которые доступны для редактирования.
# Нажмите на кнопку "Проверить" на странице.
# ВИз всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.

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
link = "https://parsinger.ru/selenium/5.5/2/1.html"




# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)
    time.sleep(3)

    elements = browser.find_elements(By.TAG_NAME, "input")

# Перебирает каждый найденный элемент в списке elements
    for element in elements:
         if not element.get_attribute('disabled'): 
            element.clear()
    # Чистит текст в каждый элемент ввода

# Перебирает каждый найденный элемент в списке elements
    for element in elements:
# Проверяем, включен ли элемент, используя метод .is_enabled(), если элемент включен, то
        if element.is_enabled():

# Проверяем, не имеет ли элемент атрибут 'disabled', если у элемента нет атрибута 'disabled'
#        if not element.get_attribute('disabled'):

# то очищаем его содержимое
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

