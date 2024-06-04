# импортирует необходимые библиотеки
импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах,
from selenium.webdriver.support.ui import Select
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# ссылка на страницу
link = "https://suninjuly.github.io/selects1.html"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)
# ищет элементы с числами и получает из них текст
    a_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']").text
    b_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']").text
# преобразует значения в числовые и складывает их
    sum = (int(a_element)+int(a_element))

# ищет выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
# выбирает опции в выпадающем списке по значению равной сумме чисел
    select1.select_by_value(str(sum))
    
# нажимает кнопку 'submit'   
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


    # успеваем скопировать код за 10 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # браузер закроется автоматически после завершения блока `with`

# не забывает оставить пустую строку в конце файла
