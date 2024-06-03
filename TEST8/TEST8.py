# Незарегистрированный пользователь, переходит по ссылке, ищет элемент с числами, считает сумму чисел, выбирает в выпадающем списке элемент с значением суммы, кликает submit 


from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    b = b_element.text
    sum = (int(a)+int(b))
    
    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_value(str(sum)) # ищет элемент с текстом переменной "sum"
    
   
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
