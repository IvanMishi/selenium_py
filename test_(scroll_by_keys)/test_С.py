import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver import Keys # Импортируется класс Keys из модуля webdriver библиотеки Selenium, который содержит специальные клавиши, такие как ENTER, ESC и TAB, для имитации нажатий в автоматизированных тестах веб-приложений.


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
                try:
                    # Прокручивает элемент в видимую область и кликает на него
                    webdriver.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                    tag_input.click()  # Клик по элементу
                    text = tag_text.text # Получает текст из элемента

                    # Обработка текста и добавление чисел
                    number = int(text)  # Пробует конвертировать текст в число
                    sum_of_numbers += number  # Добавляет к общей сумме
                    list_input.append(tag_input)  # Добавляет обработанный элемент в список

                    # Проверяет наличие элементов с классом last-of-list
                    last_of_list_elements = webdriver.find_elements(By.CSS_SELECTOR, "span.last-of-list")
                    # Проверяет условие для завершения цикла while
                    if last_of_list_elements:
                        found_last_element = True  # Устанавливаем флаг, если нашли элемент
                        break  # Выходим из текущего цикла, так как нужные элементы найдены
                # Обработка ошибки
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
                    
        # Если нашлись элементы, выходим из основного цикла
        if found_last_element:  
            break
            
            
print(f"Сумма чисел из элементов: {sum_of_numbers}")

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`