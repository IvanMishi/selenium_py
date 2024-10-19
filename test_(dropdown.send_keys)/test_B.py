import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/7/7.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит элементы выпадающего списка
    dropdown_elements = webdriver.find_elements(By.CSS_SELECTOR, "option[value]")

    # Инициализируем переменную total_sum как 0, чтобы начать с нулевой суммы
    total_sum = 0
    # Перебирает каждый найденный элемент в списке dropdown_elements
    for element in dropdown_elements:
        # Преобразует текст элемента в число и сохраняет в переменную number, при успехе продолжает выполнение кода.
        try:
            number = int(element.text)
            # Суммирует резултат
            total_sum += number
        # При возникновении исключения ValueError переходит к следующему элементу, не прерывая выполнение программы.
        except ValueError:
            # Если текст элемента не числовой, пропускает его.
            continue

    # После вызова find_elements() нельзя использовать send_keys() напрямую, так как это не метод списка.
    # Находит поле для ввода и вводит значение total_sum
    input = webdriver.find_element(By.CSS_SELECTOR, "[id='input_result']").send_keys(total_sum)
    # Нажимает кнопку отправки формы на веб-странице.
    button = webdriver.find_element(By.CSS_SELECTOR, "[type='button']").click()

    # Выводит значение переменной с id='result' в качестве ответа.
    print(f'Ответ:{webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`