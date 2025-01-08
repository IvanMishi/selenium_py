# Используйте Selenium для открытия заданного веб-сайта.

# В элементе с id="result" иногда появляется число — это и есть ваше сокровище. Проблема в том, что оно появляется очень редко. Вам придется обновлять страницу множество раз, пока не увидите это число.

# Как только число появится, скопируйте его и вставьте в предназначенное для этого поле ответа на вашем курсе.

# Для решения этой задачи используйте. browser.refresh()
# Запускает в режиме '--headless'
# Считает сколько раз обновилаь страница 

# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 




# ссылка на страницу 
link = "https://parsinger.ru/methods/1/index.html"




# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)





    while True:
        try:
            actual_result = browser.find_element(By.CSS_SELECTOR, "[id='result']").text
            if actual_result.isdigit():  # Проверка на число
                break  # Выход из цикла, если текст найден в элементе
        except NoSuchElementException:
            pass
    
        browser.refresh()
    time.sleep(2)




# выводит значение переменной actual_result в консоль
    print('Ответ', actual_result)

# оставляет пустую строку в конце файла

