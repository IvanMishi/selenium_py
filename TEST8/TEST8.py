from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']").text
    b_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']").text
    sum = (int(a_element)+int(a_element))

# Ищет выпадающий список <select> с дочерними элементами <option>, у каждого из которых есть атрибут value
    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
# Выбирает опции в выпадающем списке по значению
    select1.select_by_value(str(sum))
    
   
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забывает оставить пустую строку в конце файла
