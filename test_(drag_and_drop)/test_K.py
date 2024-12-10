# импортирует модуль time для работы с ожиданием
import time

# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

#from selenium.webdriver import Keys

# ссылка на страницу
link = "https://parsinger.ru/selenium/5.7/5/index.html"
start = time.time()
# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as webdriver:
    # открывает браузер Chrome

    # переходит по ссылке
    webdriver.get(link)
    time.sleep(2)

    count = 0
    sum_of_numbers = 0  # Переменная для хранения суммы чисел
    count = 0
    parrent = webdriver.find_elements(By.CSS_SELECTOR, "[id='main_container'] button")

    for element in parrent:
        #webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
        text = element.get_attribute('value')
        ActionChains(webdriver).click_and_hold(element).pause(float(text)).release(element).perform()
        print(text)
        count+=1
        #webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)

    time.sleep(2)
    print(count)
    print(f'Time is running{time.time() - start}')
    alert_text = webdriver.s