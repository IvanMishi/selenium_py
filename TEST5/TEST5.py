# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# ссылка на страницу 
link = "http://suninjuly.github.io/find_xpath_form"

# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае
try:
# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

# находит и заполняет поле input1 с помощью правил на основе X-path
    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("Ivan")
# находит и заполняет поле input2 с помощью правил на основе X-path
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Petrov")
# находит и заполняет поле input3 с помощью правил на основе X-path
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input3.send_keys("Smolensk")
# находит и заполняет поле input4 с помощью правил на основе X-path
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("Russia") 

# находит элемент кнопку с помощью правил на основе X-path и нажимает на нее
    btn = browser.find_element(By.XPATH, "//button[@type='submit']")
    btn.click()

finally:
    # успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла
