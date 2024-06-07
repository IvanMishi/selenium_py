# Незарегистрированный пользователь, переходит по ссылке,
считывает данные для переменной x, 
считает математическую функцию от x, 
скроллит вниз, 
вводит ответ в текстовое поле, 
выбирает чекбокс "I'm the robot", 
переключает радиокнопку в Robots rule!", 
кликает submit 


import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
   
    id="answer"
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)

 
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    

    check1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    check1.click()
    
    radio1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio1.click()
    

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
