# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# ссылка на страницу 
link = "http://suninjuly.github.io/huge_form.html"

# если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.
try:
    # открывает браузер Chrome
    browser = webdriver.Chrome()
    # переходит по ссылке
    browser.get(link)
    
    # Поиск внутри списка элементов: находит все элементы на странице, которые являются элементами ввода (input) c помощью метода find_elements()
    elements = browser.find_elements(By.TAG_NAME, "input")
    # Перебирает каждый найденный элемент в списке elements
    for element in elements:
    # Вводит текст "Мой ответ" в каждый элемент ввода
        element.send_keys("Мой ответ")
        
    # находит и нажимает кнопку 'submit'
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    # получает alert на веб-странице
    alert = browser.switch_to.alert
    # выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()


# код внутри блока finally будет выполнен в любом случае
finally:
    # закрывает браузер
    browser.quit()

# оставляет пустую строку в конце файла