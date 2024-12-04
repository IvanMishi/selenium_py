#  Работает с каждым куки по ссылке Кодовое имя: Операция "Бессмертный Печенюшка" COOKIE

# Откройте основной сайт с помощью Selenium.

# На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.
# Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry']. Сохраняйте эти данные для последующего сравнения.

# После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни. С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>

# Вставьте полученное число в специальное поле для степик.


# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
# импортирует модуль math, который предоставляет математические функции
import math 
# Вывод функции pprint форматируется так, чтобы делать структуру данных более понятной и удобной для анализа.
from pprint import pprint




# ссылка на страницу 
link = "https://parsinger.ru/methods/5/index.html"


# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:

# открывает браузер Chrome
    browser = webdriver.Chrome()
# переходит по ссылке
    browser.get(link)

# инициализирует пустой словарь для связи значений куки 'expiry' с INT из элемента <p id="result">INT</p>
    expiry_to_int_mapping = {}   

# 
    links = browser.find_elements(By.CSS_SELECTOR, "[class='urls']")
    # проходит по каждой ссылке
    for link in links:
    # переходит на найденную ссылку
        link.click()    
    # получает все куки из этой ссылки
        cookies = browser.get_cookies()
    # парсит значение INT из элемента <p id="result">INT</p> из ссылки
        int_value = int(browser.find_element(By.ID, "result").text)
    # проходит по каждой куки и проверяем наличие ключа 'expiry'
        for cookie in cookies:
            if 'expiry' in cookie:
                expiry_value = int(cookie['expiry'])
                expiry_to_int_mapping[expiry_value] = int_value
    # возвращается назад после сбора данных из ссылки
        browser.back()


# Находим самое большое значение куки 'expiry'
    max_expiry_value = max(expiry_to_int_mapping.keys(), default=None)
    if max_expiry_value is not None:
        max_int_value = expiry_to_int_mapping[max_expiry_value]
        print(f"Самое большое значение куки 'expiry' относится к числу: {max_int_value}")
    else:
        print("Куки с ключом 'expiry' не найдены.")


# оставляет пустую строку в конце файла
