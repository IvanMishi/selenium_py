import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver import Keys # Импортируется класс Keys из модуля webdriver библиотеки Selenium, который содержит специальные клавиши, такие как ENTER, ESC и TAB, для имитации нажатий в автоматизированных тестах веб-приложений.

# Ссылка на страницу.
link = 'http://parsinger.ru/selenium/6/6.html'
# Измеряет время выполнения.
start = time.time()


with (webdriver.Chrome() as webdriver):  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит элемент с математическим выражением и сохраняет текст из этого элемента в переменную x.
    x = webdriver.find_element(By.CSS_SELECTOR, "[id='text_box']").text
    # Выбирает из выпадающего списка опцию, вычисленную из переменной x с помощью eval().
    dropdown_element = webdriver.find_element(By.TAG_NAME, "select")
    dropdown_element.send_keys(str(eval(x)))
    dropdown_element.send_keys(Keys.RETURN)  # имитация подтверждения через клавиатуру
    time.sleep(1)  # Визуально убеждается, что в выпадающем списке была выбрана опция

    # Нажимает кнопку отправки формы на веб-странице.
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='button']").click()

    # Выводит значение переменной с id='result' в качестве ответа.
    print(f'Ответ:{webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`