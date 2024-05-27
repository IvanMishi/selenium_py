#Незарегестрированный пользователь, переходит по ссылке, считывает данные в переменную - x, выполняет данные переменной и вводит результат в текстовое поле, ставит отметку checkbox "I'm the robot", выбрать radiobutton "Robots rule!", кликает Submit

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)



    input1 = browser.find_element(By.CSS_SELECTOR, "[class='form-control']")
    input1.send_keys(y)

    check1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    check1.click()
    
    radio1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio1.click()
    

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
