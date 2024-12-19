import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver import Keys  # Импортируется класс Keys из модуля webdriver библиотеки Selenium, который содержит специальные клавиши, такие как ENTER, ESC и TAB, для имитации нажатий в автоматизированных тестах веб-приложений.


# ссылка на страницу
link = "http://parsinger.ru/infiniti_scroll_1/"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    list_input = []  # Инициализирут пустой список для хранения обработанных элементов ввода
    sum_of_numbers = 0  # Переменная для хранения суммы чисел


    while True:
        # Ищет все элементы input и text на веб-странице
        input_tags = webdriver.find_elements(By.CSS_SELECTOR, "#scroll-container span input")
        text_tags = webdriver.find_elements(By.CSS_SELECTOR, "#scroll-container span")

        # Обходит каждый элемент input в списке
        found_last_element = False  # Флаг, показывающий, найден ли элемент last-of-list
        for tag_input, tag_text in zip(input_tags, text_tags):
            # Проверяет, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:

                # Прокручивает элемент в видимую область и кликает на него
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                tag_input.click()  # Клик по элементу
                text = tag_text.text  # Получает текст из элемента

                # Обработка текста и добавление чисел
                number = int(text)  # Пробует конвертировать текст в число
                sum_of_numbers += number  # Добавляет к общей сумме
                list_input.append(tag_input)  # Добавляет обработанный элемент в список

                # Проверяет условие для завершения цикла while
                if webdriver.find_elements(By.CSS_SELECTOR, "span.last-of-list"): # Если найден элемент с классом last-of-list
                    found_last_element = True  # Устанавливаем флаг, если нашли элемент
                    break  # Выходим из текущего цикла, так как нужные элементы найдены

        # Если нашлись элементы, выходим из основного цикла
        if found_last_element:
            break

print(f"Сумма чисел из элементов: {sum_of_numbers}")


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`