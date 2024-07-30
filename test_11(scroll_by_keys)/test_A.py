# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
# Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span ​​​​​​​<span id="result1">954</span>
# Вычисление: Соберите все эти числа и сложите их. 




# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


# ссылка на страницу
link = "https://parsinger.ru/scroll/2/index.html"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:
    # открывает браузер Chrome
    browser = webdriver.Chrome()
    # переходит по ссылке
    browser.get(link)


    total_sum = 0
    convertible_count = 0
    unconvertible_count = 0
    # Ищет все родительские элементы на странице, с
    parent_elements = browser.find_elements(By.CSS_SELECTOR, "[class='item']")

    for child_element in parent_elements:
        checkbox_btn_element = child_element.find_element(By.CSS_SELECTOR, "[type='checkbox']")
        checkbox_btn_element.send_keys(Keys.DOWN)
        checkbox_btn_element.click()
        text_element = child_element.find_element(By.XPATH, ".//span[contains(@id, 'result')]")
        text = text_element.text

        # В блоке "try" помещается код, который нужно выполнить. Если в ходе выполнения кода возникает исключение, выполнение переходит к блоку "except".
        # Если текст найден, то попытется преобразовать текст в число и добавить его к общей сумме и увеличить счетчик успешно преобразованных элементов
        try:
            num = int(text)
            total_sum += num
            convertible_count += 1
        # Использование "except ValueError:" означает обработку исключительно ошибок, связанных с значением (тип ValueError).
        # Если невозможно преобразовать в число, увеличить счетчик элементов, которые нельзя преобразовать
        except ValueError:
            unconvertible_count += 1


    print("Общая сумма найденых чисел:", total_sum)
    print("Количество элементов, которые содержат число:", convertible_count)
    print("Количество элементов, которые не содержат число:", unconvertible_count)





       