import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# ссылка на страницу
link = "https://parsinger.ru/selenium/5.7/1/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная для хранения количества найденных элементов.
count = 0


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    parrent = webdriver.find_elements(By.CSS_SELECTOR, "[class='button-container']")
    for element in parrent:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        count += 1

    time.sleep(1)
    print(f'Количество найденных элементов: {count}')
    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит  значение полученного текста из alert в консоль в качестве ответа
    print(f'Ответ: {actual_result}')
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
