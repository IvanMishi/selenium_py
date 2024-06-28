# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль re, который позволяет работать с регулярными выражениями для поиска, замены и обработки текстовых данных по заданным правилам.
import re


# ссылка на страницу 
link = "http://suninjuly.github.io/find_xpath_form"


# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае
try:
    # открывает браузер Chrome
    driver = webdriver.Chrome()
    # переходит по ссылке
    driver.get(link)

    # находит и заполняет поле "First name" с помощью правил на основе X-path
    input_first_name = driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Ivan")
    # находит и заполняет поле "Last name" с помощью правил на основе X-path
    input_last_name = driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Petrov")
    # находит и заполняет поле "City" с помощью правил на основе X-path
    input_city = driver.find_element(By.XPATH, "//input[@class='form-control city']").send_keys("Smolensk")
    # находит и заполняет поле "Country" с помощью правил на основе X-path
    input_county = driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Russia") 

    # находит кнопку "Submit" с помощью правил на основе X-path и нажимает на нее
    button_submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # получает alert на веб-странице
    alert = driver.switch_to.alert
    # выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

except ValueError as e:
    print(f"Произошла ошибка при обработке значений на веб-странице: {e}")
    

# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    driver.quit()

# оставляет пустую строку в конце файла
