import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'http://parsinger.ru/selenium/6/6.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит элемент с математическим выражением и сохраняет текст из этого элемента в переменную x.
    x = webdriver.find_element(By.CSS_SELECTOR, "[id='text_box']").text
    # Выбирает из выпадающего списка опцию, вычисленную из переменной x с помощью eval().
    dropdown_element = webdriver.find_element(By.TAG_NAME, "select").send_keys(str(eval(x)))
    time.sleep(1)  # Визуально убеждается, что в выпадающем списке была выбрана опция

    # Нажимает кнопку отправки формы на веб-странице.
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='button']").click()

    # Сохраняет текст элемента на странице в переменную result.
    result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text
    # Выводит значение переменной result в консоль в качестве ответа
    print('Ответ', result)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`