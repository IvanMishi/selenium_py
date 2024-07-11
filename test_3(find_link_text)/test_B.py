# Импортирует необходимые библиотеки
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# Ссылка на страницу
link = "http://parsinger.ru/selenium/2/2.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

#Искомый элемент на веб-странице — это ссылка <a href="16243162441624.html">16243162441624</a>, которая содержит текст "16243162441624".
expected_result = '16243162441624'
# Переменная для поиска ссылки по частичному тексту
link_text_fragment = '162431'


# Блок try используется для выполнения кода, который может вызвать исключение
try:
    # Открывает браузер Chrome
    webdriver = webdriver.Chrome()
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Находит ссылку с подстрокой из переменной link_text_fragment
    element_link = webdriver.find_element(By.PARTIAL_LINK_TEXT, link_text_fragment)
    # Записывает текст из ссылки в переменную
    actual_result = element_link.text
    # Нажимает на ссылку
    element_link.click()

    # Записывает в переменную текст, который появится в теге найденной страницы
    result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text

    #Выводит в консоль ответ
    print(f'Ответ: {result}')

    # Если текст ссылки верен, дополнительные сообщения в консоли не должны выводиться.
    assert actual_result == expected_result, f"Текст ссылки не соответствует ожидаемому. Полученный текст: {actual_result}, Ожидаемый текст: {expected_result}"


# Код внутри блока finally будет выполнен в любом случае
finally:
    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")

    # Закрывает браузер
    webdriver.quit()

# Не забывает оставить пустую строку в конце файла
