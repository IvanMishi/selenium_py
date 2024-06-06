# импортирует необходимые библиотеки

# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# ссылка на страницу 
link = "http://parsinger.ru/selenium/6/6.html"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

# ищет элемент с математическим выражением и сохраняет текст из этого элемента в переменную x
    x = browser.find_element(By.CSS_SELECTOR, "[id='text_box']").text  
# выбирает в выпадающем списке на странице опцию с текстовым значением, вычисленным из переменной x с помощью eval()
    element = browser.find_element(By.TAG_NAME, "select").send_keys(str(eval(x)))

# нажимает кнопку 'submit'  
    button = browser.find_element(By.CSS_SELECTOR, "[type='button']").click()

# сохраняет текст из элемента, появившегося на странице в переменную actual_result
    actual_result = browser.find_element(By.CSS_SELECTOR, "[id='result']").text
# выводит значение переменной actual_result в консоль
    print('Ответ', actual_result)

# оставляет пустую строку в конце файла
