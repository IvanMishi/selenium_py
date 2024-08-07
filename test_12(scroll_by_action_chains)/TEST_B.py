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
link = "https://parsinger.ru/infiniti_scroll_2/"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:
    # открывает браузер Chrome

    # переходит по ссылке
    browser.get(link)
    time.sleep(2)
    #actual_result = int(2691483484)

    sum_of_numbers = 0  # Переменная для хранения суммы чисел
    count = 0
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    for _ in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 5000).perform()

    flag = True
    while flag:
        for element in div.find_elements(By.XPATH, '//*[@id="scroll-container"]/p'):
            num = element.text
            sum_of_numbers+=int(num)
            count+=1
            print(f'элемент{count}, с числом{num}, общаяя сумма {sum_of_numbers}')
            if element.get_attribute('class') == 'last-of-list':
                flag = False

    print(f"Сумма чисел из элементов: {sum_of_numbers}")
    #assert actual_result == sum_of_numbers