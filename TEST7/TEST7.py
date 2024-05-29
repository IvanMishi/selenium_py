# Незарегестрированный пользователь, переходит по ссылке, ищет картинку(сундук с сокровищами отмечает чек-бокс, выбирает радиокнопку (Robots rule!), кликает submit 

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/get_attribute.html"


# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

    browser = webdriver.Chrome()
    browser.get(link)

 
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)


    input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    input1.send_keys(y)

    check1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    check1.click()

    radio1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio1.click()

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()

    # успеваем скопировать код за 10 секунд
    time.sleep(10)
# Браузер закроется автоматически после завершения блока `with`

# не забываем оставить пустую строку в конце файла
