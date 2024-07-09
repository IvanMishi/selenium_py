# Импортирует необходимые библиотеки
# Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
from selenium.webdriver.support.ui import Select
# Импортирует модуль time для работы с ожиданием
import time
# Импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# Импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By



# Ссылка на страницу
link = "http://parsinger.ru/selenium/6/6.html"

# Измеряет время выполнения определенного участка кода.
start = time.time()

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
# Открывает браузер Chrome
with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    # Находит элемент с математическим выражением и сохраняет текст из этого элемента в переменную x
    x = webdriver.find_element(By.CSS_SELECTOR, "[id='text_box']").text  
    # Выбирает в выпадающем списке на странице опцию с текстовым значением, вычисленным из переменной x с помощью eval()
    dropdown_element = webdriver.find_element(By.TAG_NAME, "select").send_keys(str(eval(x)))

    # Нажимает кнопку отправки формы на веб-странице
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='button']").click()

    # Cохраняет текст из элемента, появившегося на странице в переменную result
    result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text
    # Dыводит значение переменной actual_result в консоль
    print('Ответ', result)

    # Измеряет время выполнения кода и выводит его в консоль.
    print(f'Time is running {time.time() - start}')

    # Браузер закроется автоматически после завершения блока `with`
    # Не забывает оставить пустую строку в конце файла
