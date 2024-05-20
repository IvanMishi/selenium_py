

import time #
import math #
from selenium import webdriver #
from selenium.webdriver.common.by import By #

 
link = "http://suninjuly.github.io/find_link_text"
# переменная с мат выражением
m = str(math.ceil(math.pow(math.pi, math.e)*10000))


# для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,  использует конструкцию try/finally
try:
    browser = webdriver.Chrome()
    browser.get(link)

# метод find_element, который принимает два аргумента - тип локатора и значение локатора

# поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки
    button = browser.find_element(By.PARTIAL_LINK_TEXT, m)
    button.click()

# поиск элемента по названию тега элемента
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

# поиск по атрибуту name элемента
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

# поиск по значению атрибута class
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")

# поиск по уникальному атрибуту id элемента. этот метод наиболее стабильный
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

# поиск элемента с помощью правил на основе CSS. это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    #  успевает скопировать код за 10 секунд
    time.sleep(10)
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла
