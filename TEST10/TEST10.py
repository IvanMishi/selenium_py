# импортирует необходимые библиотеки

# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "https://SunInJuly.github.io/execute_script.html"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.

with webdriver.Chrome() as browser:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    
    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(calc(x_element))

 
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
#
    check = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
#    
    radio = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


# получает alert на веб-странице
    alert = browser.switch_to.alert
    # сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # ждет 2 секунды
    time.sleep(2)
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()
# выводит значение переменной actual_result в консоль
    print('Ответ', actual_result)

    # браузер закроется автоматически после завершения блока `with`
# оставляет пустую строку в конце файла
