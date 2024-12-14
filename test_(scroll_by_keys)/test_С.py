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

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    sum_of_numbers = 0  # Переменная для хранения суммы чисел

    # Флаг для проверки наличия элемента с классом last-of-list
    found_last_of_list = False

    while True:
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = browser.find_elements(By.CSS_SELECTOR, "#scroll-container span input")
        text_tags = browser.find_elements(By.CSS_SELECTOR, "#scroll-container span")

        # Обходим каждый элемент input в списке
        for tag_input, tag_text in zip(input_tags, text_tags):
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                tag_input.click()  # Кликаем на элемент
                text = tag_text.text
                try:
                    number = int(text)
                except ValueError:
                    # Если текст не удалось преобразовать в число, пропускаем этот элемент
                    continue
                sum_of_numbers += number  # Суммируем числа
                list_input.append(tag_input)

        # Проверяем условие для завершения цикла while
        if len(input_tags) == 100:
            break
    print(f"Сумма чисел из элементов: {sum_of_numbers}")





       